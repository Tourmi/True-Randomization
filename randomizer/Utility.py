from typing import Any, Optional, Literal, TypeVar
import json

from .GlobalImports import *
from . import FileType

T = TypeVar('T')

def read_json(filepath : str):
    with open(filepath, "r", encoding="utf8") as file_reader:
        return json.load(file_reader)

def read_json_files(directory : str) -> dict[str, Any]:
    result : dict[str, Any] = {}
    for file in os.listdir(directory):
        name, _ = os.path.splitext(file)
        result[name] = read_json(f"{directory}\\{file}")
    return result

def write_json(filepath : str, obj : Any):
    with open(filepath, "w", encoding="utf8") as file_writer:
        file_writer.write(json.dumps(obj, ensure_ascii=False, indent=2))

def get_file_type(assetpath : str) -> FileType:
    if "DataTable" in assetpath:
        return FileType.DataTable
    if "StringTable" in assetpath:
        return FileType.StringTable
    if "Level" in assetpath:
        return FileType.Level
    if "Material" in assetpath:
        return FileType.Material
    if "Texture" in assetpath or "UI" in assetpath and not "StartupSelecter" in assetpath and not "Title" in assetpath:
        return FileType.Texture
    if "Sound" in assetpath:
        return FileType.Sound
    
    return FileType.Blueprint

def simplify_item_name(name):
    return name.replace("Familiar:", "").replace(" ", "").replace("'", "").replace("-", "").replace(".", "").replace("é", "e").replace("è", "e").replace("&", "and").lower()

def remove_inst_number(name : str) -> str:
    """
    Return a string without its instance number the same way Unreal does it
    """
    split_name = name.split("_")
    if split_name[-1][0] != "0":
        try:
            int(split_name[-1])
            split_name.pop()
        except ValueError:
            pass
    return "_".join(split_name)

def unreal_to_python_data(struct, unreal_type : Optional[str] = None):
    unreal_type = unreal_type if unreal_type else str(struct.PropertyType)
    match unreal_type:
        case "ArrayProperty":
            array = []
            for array_item in struct.Value:
                array.append(unreal_to_python_data(array_item, str(struct.ArrayType)))
            return array
        case "ByteProperty":
            return str(struct.EnumValue)
        case "FloatProperty":
            return round(struct.Value, 3)
        case "EnumProperty":
            return str(struct.Value)
        case "NameProperty":
            return str(struct.Value)
        case "ObjectProperty":
            return struct.Value.Index
        case "SoftObjectProperty":
            return str(struct.Value.AssetPath.AssetName)
        case "StrProperty":
            return str(struct.Value) if struct.Value else ""
        case "StructProperty":
            dictionary = {}
            for dict_item in struct.Value:
                dictionary[str(dict_item.Name)] = unreal_to_python_data(dict_item)
            return dictionary
        case "TextProperty":
            return str(struct.CultureInvariantString) if struct.CultureInvariantString else ""
        case _:
            return struct.Value

def python_to_unreal_data(value, struct, uasset, unreal_type : Optional[str] =None):
    unreal_type = unreal_type if unreal_type else str(struct.PropertyType)
    match unreal_type:
        case "ArrayProperty":
            array = []
            for array_item in value:
                sub_struct = create_unreal_struct(str(struct.ArrayType), struct.DummyStruct)
                python_to_unreal_data(array_item, sub_struct, uasset, str(struct.ArrayType))
                array.append(sub_struct)
            struct.Value = array
        case "ByteProperty":
            struct.EnumValue = FName.FromString(uasset, value)
        case "EnumProperty":
            struct.Value = FName.FromString(uasset, value)
        case "NameProperty":
            struct.Value = FName.FromString(uasset, value)
        case "ObjectProperty":
            struct.Value = FPackageIndex(value)
        case "SoftObjectProperty":
            struct.Value = FSoftObjectPath(None, FName.FromString(uasset, value), None) # type: ignore
        case "StrProperty":
            struct.Value = FString(value) if value else None
        case "StructProperty":
            for dict_item in struct.Value:
                python_to_unreal_data(value[str(dict_item.Name)], dict_item, uasset)
        case "TextProperty":
            struct.CultureInvariantString = FString(value) if value else None
        case _:
            struct.Value = value

def unreal_to_unreal_data(value, struct, unreal_type : Optional[str] = None):
    unreal_type = unreal_type if unreal_type else str(struct.PropertyType)
    match unreal_type:
        case "ByteProperty":
            struct.EnumValue = value
        case "TextProperty":
            struct.CultureInvariantString = value
        case _:
            struct.Value = value

def create_unreal_struct(unreal_type : str, dummy_struct=None):
    match unreal_type:
        case "BoolProperty":
            return BoolPropertyData()
        case "ByteProperty":
            struct = BytePropertyData()
            struct.ByteType = BytePropertyType.FName
            return struct
        case "EnumProperty":
            return EnumPropertyData()
        case "FloatProperty":
            return FloatPropertyData()
        case "IntProperty":
            return IntPropertyData()
        case "NameProperty":
            return NamePropertyData()
        case "SoftObjectProperty":
            return SoftObjectPropertyData()
        case "StrProperty":
            return StrPropertyData()
        case "StructProperty":
            return dummy_struct
        case "TextProperty":
            return TextPropertyData()
        case _:
            raise Exception(f"Unsupported property type: {unreal_type}")

def squircle(value : float, exponent : float) -> float:
    return -(1-value**exponent)**(1/exponent)+1

def invert_squircle(value : float, exponent : float) -> float:
    return (1-(-value+1)**exponent)**(1/exponent)

def pick_and_remove(list : list[T]) -> T:
    item = random.choice(list)
    list.remove(item)
    return item

def random_weighted(value : float, minimum : float, maximum : float, step : float, exponent : float, adaptive = True) -> float:
    full_range = maximum - minimum
    if random.randint(0, 1) > 0:
        distance = maximum - value
        if adaptive:
            exponent = (exponent-1)*(0.5*4**(distance/full_range))+1
        return round(round((value + squircle(random.random(), exponent)*distance)/step)*step, 3)
    else:
        distance = value - minimum
        if adaptive:
            exponent = (exponent-1)*(0.5*4**(distance/full_range))+1
        return round(round((value - squircle(random.random(), exponent)*distance)/step)*step, 3)

def split_enemy_profile(profile : str) -> tuple[str, Literal['Normal', 'Hard', '']]:
    difficulty = ""
    enemy_id = profile
    if "Normal" in profile:
        enemy_id = profile.replace("_Normal", "")
        difficulty = "Normal"
    if "Hard" in profile:
        enemy_id = profile.replace("_Hard", "")
        difficulty = "Hard"
    return (enemy_id, difficulty)
