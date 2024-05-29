from typing import Any

from .GlobalImports import *
from .Constants import *
from . import Utility
from . import FileType

type Datatable = dict[str, dict[str, dict[str, Any]]]

_LOAD_TYPES = [
    FileType.DataTable,
    FileType.Level,
    FileType.StringTable,
    FileType.Blueprint,
    FileType.Material,
    FileType.Sound
]

_SIMPLIFY_TYPES = [
    FileType.DataTable,
    FileType.StringTable
]

class Data:
    @classmethod
    def reload_data(cls):
        cls.datatable : Datatable = {}
        cls.stringtable : dict[str, dict[str, str]] = {}
        cls.file_to_path : dict[str, str] = Utility.read_json("Data\\FileToPath.json")
        cls.file_to_type : dict[str, FileType] = {filepath:Utility.get_file_type(filepath) for filepath in cls.file_to_path.values()}
        cls.constant = Utility.read_json_files("Data\\Constant")
        cls.translation : dict[str, dict[str, str]] = Utility.read_json_files("Data\\Translation")
        cls.load_start_item_translations()
    
    @classmethod
    def load_game_data(cls):
        cls.game_data : dict[str, UAsset] = {}
        for file, filetype in Data.file_to_type.items():
            if filetype in _LOAD_TYPES:
                extension = ".umap" if filetype == FileType.Level else ".uasset"
                cls.game_data[file] = UAsset(f"{ASSETS_DIR}\\{Data.file_to_path[file]}\\" + file.split("(")[0] + extension, EngineVersion.VER_UE4_22)

    @classmethod
    def load_start_item_translations(cls):
        cls.start_item_translation : dict[str, str] = {}
        for type in ["Item", "Shard"]:
            for entry in cls.translation[type]:
                cls.start_item_translation[Utility.simplify_item_name(cls.translation[type][entry])] = entry

    @classmethod
    def table_complex_to_simple(cls):
        """
        The uasset data is inconvenient to access and would take up too much text space in the code\n
        Convert them to a simplified dictionary that is similar to the old serializer's outputs
        """
        cls.original_datatable : Datatable = {}
        cls.datatable_entry_index : dict[str, dict[str, int]] = {}
        for file in cls.file_to_type:
            if cls.file_to_type[file] in _SIMPLIFY_TYPES:
                if cls.file_to_type[file] == FileType.DataTable:
                    cls.datatable[file] = {}
                    for entry in cls.game_data[file].Exports[0].Table.Data:
                        cls.datatable[file][str(entry.Name)] = {}
                        for data in entry.Value:
                            cls.datatable[file][str(entry.Name)][str(data.Name)] = Utility.unreal_to_python_data(data)
                    cls.original_datatable[file] = copy.deepcopy(cls.datatable[file])
                    cls.datatable_entry_index[file] = {}
                elif cls.file_to_type[file] == FileType.StringTable:
                    cls.stringtable[file] = {}
                    for entry in cls.game_data[file].Exports[0].Table:
                        cls.stringtable[file][str(entry.Key)] = str(entry.Value)

    @classmethod
    def table_simple_to_complex(cls):
        """
        Convert the simplified datatables back to their complex versions
        """
        for file in cls.file_to_type:
            if cls.file_to_type[file] in _SIMPLIFY_TYPES:
                if cls.file_to_type[file] == FileType.DataTable:
                    entry_count = 0
                    for entry in cls.datatable[file]:
                        #If the datatables had entries added then add an entry slot in the uasset too
                        if entry_count >= cls.game_data[file].Exports[0].Table.Data.Count:
                            cls._append_datatable_entry(file, entry)
                        data_count = 0
                        for data in cls.datatable[file][entry]:
                            #Only patch the value if it is different from the original, saves a lot of load time
                            if entry in cls.original_datatable[file]:
                                if cls.datatable[file][entry][data] == cls.original_datatable[file][entry][data]:
                                    data_count += 1
                                    continue
                            struct = cls.game_data[file].Exports[0].Table.Data[entry_count].Value[data_count]
                            Utility.python_to_unreal_data(cls.datatable[file][entry][data], struct, cls.game_data[file])
                            data_count += 1
                        entry_count += 1
                elif cls.file_to_type[file] == FileType.StringTable:
                    cls.game_data[file].Exports[0].Table.Clear()
                    for entry in cls.stringtable[file]:
                        cls.game_data[file].Exports[0].Table.Add(FString(entry), FString(cls.stringtable[file][entry]))
    

    @classmethod
    def update_datatable_order(cls):
        #Shift some datatable entry placements when necessary
        for file in cls.datatable_entry_index:
            for entry_1 in cls.datatable_entry_index[file]:
                old_index = list(cls.datatable[file]).index(entry_1)
                new_index = cls.datatable_entry_index[file][entry_1]
                current_entry = Data.game_data[file].Exports[0].Table.Data[old_index].Clone()
                Data.game_data[file].Exports[0].Table.Data.Remove(Data.game_data[file].Exports[0].Table.Data[old_index])
                Data.game_data[file].Exports[0].Table.Data.Insert(new_index, current_entry)
                #Update the other entry indexes for that same datatable
                for entry_2 in cls.datatable_entry_index[file]:
                    if new_index < old_index:
                        if new_index <= cls.datatable_entry_index[file][entry_2] < old_index:
                            cls.datatable_entry_index[file][entry_2] += 1
                    elif new_index > old_index:
                        if new_index >= cls.datatable_entry_index[file][entry_2] > old_index:
                            cls.datatable_entry_index[file][entry_2] -= 1

    @staticmethod
    def get_export_by_name(filename, export_name):
        for export in Data.game_data[filename].Exports:
            if str(export.ObjectName) == export_name:
                return export
        raise Exception("Export not found")

    @staticmethod
    def search_and_replace_string(filename, class_name, data_name, old_value, new_value):
        """
        Search for a specific piece of data to change in a blueprint file and swap it
        """
        for export in Data.game_data[filename].Exports:
            if class_name == str(Data.game_data[filename].Imports[abs(export.ClassIndex.Index) - 1].ObjectName):
                for data in export.Data:
                    if str(data.Name) == data_name and str(data.Value) == old_value:
                        data.Value = FName.FromString(Data.game_data[filename], new_value)

    @staticmethod
    def copy_asset_import(import_name, source_asset, target_asset):
        #Check if import already exists
        count = 0
        for old_import in Data.game_data[target_asset].Imports:
            count -= 1
            if import_name in str(old_import.ObjectName):
                return FPackageIndex(count)
        #Gather import information
        package_index = None
        import_indexes = []
        count = 0
        for old_import in Data.game_data[source_asset].Imports:
            if import_name in str(old_import.ObjectName) and count != package_index:
                import_indexes.append(count)
                package_index = abs(old_import.OuterIndex.Index) - 1
            count += 1
        #Add the import
        new_import_index = len(Data.game_data[target_asset].Imports)
        for index in import_indexes:
            old_import = Data.game_data[source_asset].Imports[index]
            new_import = Import(
                FName.FromString(Data.game_data[target_asset], str(old_import.ClassPackage)),
                FName.FromString(Data.game_data[target_asset], str(old_import.ClassName)),
                FPackageIndex(-(new_import_index + 1 + len(import_indexes))),
                FName.FromString(Data.game_data[target_asset], str(old_import.ObjectName)),
                True
            )
            Data.game_data[target_asset].Imports.Add(new_import) # type: ignore
        old_import = Data.game_data[source_asset].Imports[package_index] # type: ignore
        new_import = Import(
            FName.FromString(Data.game_data[target_asset], str(old_import.ClassPackage)),
            FName.FromString(Data.game_data[target_asset], str(old_import.ClassName)),
            FPackageIndex(0),
            FName.FromString(Data.game_data[target_asset], str(old_import.ObjectName)),
            True
        )
        Data.game_data[target_asset].Imports.Add(new_import) # type: ignore
        return FPackageIndex(-(new_import_index + 1))
    
    @classmethod
    def _append_datatable_entry(cls, file, entry):
        #Append a new datatable entry to the end to be edited later on
        new_entry = cls.game_data[file].Exports[0].Table.Data[0].Clone()
        new_entry.Name = FName.FromString(cls.game_data[file], entry)
        cls.game_data[file].Exports[0].Table.Data.Add(new_entry)

Data.reload_data()