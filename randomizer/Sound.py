import re

from .GlobalImports import *
from .Constants import *
from .Data import *
from . import Utility

_EVENT_SKIP = [
    "Event_09_001_2",
    "Event_09_002_2",
    "Event_09_003_2",
    "Event_10_001_2",
    "Event_10_002_2",
    "Event_10_003_2",
    "Event_10_004_2",
    "Event_10_005_2",
    "Event_10_006_2",
    "Event_10_007_2"
]

_BG_EVENTS = [
    "Train_AlchemyRoom_Enter_01",
    "Train_AlchemyRoom_Enter_02",
    "Train_ConfirmAlchemy_01",
    "Train_ConfirmAlchemy_02",
    "Train_QuitAlchemy_01",
    "Train_QuitAlchemy_02",
    "Train_AlchemyBegins_01",
    "Train_AlchemyBegins_02",
    "Train_AlchemyFinishes_01",
    "Train_AlchemyFinishes_02",
    "Train_AlchemyFinishes_03",
    "Train_AlchemyFinishes_04",
    "Train_AlchemyFinishes_05",
    "Train_AlchemyFinishes_06",
    "Train_AlchemyContinue_01",
    "Train_AlchemyContinue_02",
    "Church_An_etc_01",
    "Church_An_etc_02",
    "Church_An_etc_03",
    "Church_An_etc_04",
    "Church_An_etc_05",
    "Church_An_etc_06",
    "Church_An_etc_07",
    "Church_An_etc_09",
    "Church_An_etc_10",
    "Church_An_etc_11",
    "Church_Dominique_etc_01",
    "Church_Dominique_etc_02",
    "Church_Dominique_etc_03",
    "Church_Dominique_etc_04",
    "Church_Dominique_etc_05",
    "Church_Dominique_etc_06",
    "Church_Dominique_etc_07",
    "Church_Dominique_etc_08",
    "Church_Dominique_etc_09",
    "Church_Dominique_etc_10",
    "Qu05_N5006_010",
    "Qu06_N5008_008"
]

_MUSIC_LIST = [
    "BGM_m01SIP",
    "BGM_m03ENT",
    "BGM_m04GDN",
    "BGM_m05SAN",
    "BGM_m08TWR",
    "BGM_m07LIB",
    "BGM_m09TRN",
    "BGM_m13ARC",
    "BGM_m06KNG",
    "BGM_m11UGD",
    "BGM_m12SND",
    "BGM_m17RVA",
    "BGM_m15JPN",
    "BGM_m10BIG",
    "BGM_m18ICE",
    "BGM_m19K2C",
    "BGM_m20JRN"
]


class Sound:
    @classmethod
    def set_voice_language(cls, language : int):
        cls.voice_language = ["jp", "en"][language - 1]

    @classmethod
    def randomize_dialogues(cls):
        cls.character_to_event : dict[str, list[str]] = {}
        #Gather all events for each character
        for entry in Data.datatable["PB_DT_DialogueTableItems"]:
            if entry in _EVENT_SKIP:
                continue
            direction = Data.datatable["PB_DT_DialogueTableItems"][entry]["SpeakingPosition"].split("::")[-1]
            #Zangetsu has an event that doesn't have his name
            if entry == "Event_06_001":
                if not "Zangetsu" in cls.character_to_event:
                    cls.character_to_event["Zangetsu"] = []
                cls.character_to_event["Zangetsu"].append(entry)
            else:
                character = Utility.remove_inst_number(Data.datatable["PB_DT_DialogueTableItems"][entry][f"SpeakerID_{direction}"])
                if not character in cls.character_to_event:
                    cls.character_to_event[character] = []
                cls.character_to_event[character].append(entry)
            #Anything past this is dummy events
            if entry == "Tutorial_Open_Door":
                break
        
        #Get every event's face anim, taking in consideration that null fields inherit previous anim 
        cls.event_to_face_anim : dict[str, str] = {}
        for direction in ["Left", "Right"]:
            #Start with standard consecutions
            for entry in Data.datatable["PB_DT_DialogueTableItems"]:
                #Get anim of current event
                current_anim = Data.datatable["PB_DT_DialogueTableItems"][entry][f"FaceAnim_{direction}"]
                next_event = Data.datatable["PB_DT_DialogueTableItems"][entry]["Branches"]
                if current_anim == "None":
                    continue
                if Data.datatable["PB_DT_DialogueTableItems"][entry]["SpeakingPosition"].split("::")[-1] == direction:
                    cls.event_to_face_anim[entry] = current_anim
                if not next_event:
                    continue
                if ";" in next_event:
                    next_event = next_event.split(";")[0]
                #Get anim of following events
                while Data.datatable["PB_DT_DialogueTableItems"][next_event][f"FaceAnim_{direction}"] == "None":
                    if Data.datatable["PB_DT_DialogueTableItems"][next_event]["SpeakingPosition"].split("::")[-1] == direction:
                        cls.event_to_face_anim[next_event] = current_anim
                    next_event = Data.datatable["PB_DT_DialogueTableItems"][next_event]["Branches"]
                    if not next_event:
                        break
                    if ";" in next_event:
                        next_event = next_event.split(";")[0]
            #Loop again to get the few branching paths
            for entry in Data.datatable["PB_DT_DialogueTableItems"]:
                #Get anim of current event
                current_anim = Data.datatable["PB_DT_DialogueTableItems"][entry][f"FaceAnim_{direction}"]
                next_event = Data.datatable["PB_DT_DialogueTableItems"][entry]["Branches"]
                if current_anim == "None":
                    continue
                if not next_event:
                    continue
                if not ";" in next_event:
                    continue
                next_event = next_event.split(";")[1]
                #Get anim of following events
                while Data.datatable["PB_DT_DialogueTableItems"][next_event][f"FaceAnim_{direction}"] == "None":
                    if Data.datatable["PB_DT_DialogueTableItems"][next_event]["SpeakingPosition"].split("::")[-1] == direction:
                        cls.event_to_face_anim[next_event] = cls.event_to_face_anim[entry]
                    next_event = Data.datatable["PB_DT_DialogueTableItems"][next_event]["Branches"]
                    if not next_event:
                        break
        #Get the max text length amongst background events
        max_length = 0
        for event in _BG_EVENTS:
            if len(Data.datatable["PB_DT_DialogueTextMaster"][event]["DialogueText"]) > max_length:
                max_length = len(Data.datatable["PB_DT_DialogueTextMaster"][event]["DialogueText"])
        
        #Randomize in a dict by first giving background events short lines and then doing the rest
        cls.event_replacement : dict[str, str] = {}
        for character in cls.character_to_event:
            new_list = copy.deepcopy(cls.character_to_event[character])
            for event in cls.character_to_event[character]:
                if event in _BG_EVENTS:
                    chosen = random.choice(new_list)
                    try:
                        while len(Data.datatable["PB_DT_DialogueTextMaster"][chosen]["DialogueText"]) > max_length:
                            chosen = random.choice(new_list)
                    except KeyError:
                        pass
                    new_list.remove(chosen)
                    cls.event_replacement[event] = chosen
            for event in cls.character_to_event[character]:
                if not event in _BG_EVENTS:
                    chosen = random.choice(new_list)
                    new_list.remove(chosen)
                    cls.event_replacement[event] = chosen
        #Apply the changes
        for event in cls.event_replacement:
            direction = Data.datatable["PB_DT_DialogueTableItems"][event]["SpeakingPosition"].split("::")[-1]
            Data.datatable["PB_DT_DialogueTableItems"][event][f"FaceAnim_{direction}"] = cls.event_to_face_anim[cls.event_replacement[event]] if cls.event_replacement[event] in cls.event_to_face_anim else "None"
            try:
                Data.datatable["PB_DT_DialogueTextMaster"][event]["DialogueText"]    = Data.original_datatable["PB_DT_DialogueTextMaster"][cls.event_replacement[event]]["DialogueText"]
                Data.datatable["PB_DT_DialogueTextMaster"][event]["DialogueAudioID"] = Data.original_datatable["PB_DT_DialogueTextMaster"][cls.event_replacement[event]]["DialogueAudioID"]
                Data.datatable["PB_DT_DialogueTextMaster"][event]["JPLipRef"]        = Data.original_datatable["PB_DT_DialogueTextMaster"][cls.event_replacement[event]]["JPLipRef"]
                Data.datatable["PB_DT_DialogueTextMaster"][event]["ENLipRef"]        = Data.original_datatable["PB_DT_DialogueTextMaster"][cls.event_replacement[event]]["ENLipRef"]
            except KeyError:
                pass
            try:
                Data.datatable["PB_DT_SoundMaster"][f"{cls.voice_language}_{event}_SE"]["AssetPath"] = Data.original_datatable["PB_DT_SoundMaster"][f"{cls.voice_language}_{cls.event_replacement[event]}_SE"]["AssetPath"]
            except KeyError:
                pass

    @classmethod
    def randomize_music(cls):
        new_list = copy.deepcopy(_MUSIC_LIST)
        random.shuffle(new_list)
        cls.music_replacement = dict(zip(_MUSIC_LIST, new_list))
        for music_id in cls.music_replacement:
            if not music_id in Data.datatable["PB_DT_SoundMaster"]:
                continue
            replacement = cls.music_replacement[music_id]
            Data.datatable["PB_DT_SoundMaster"][music_id]["AssetPath"] = f"/Game/Core/Sound/bgm/{replacement}.{replacement}"

    @classmethod
    def update_lip_movement(cls):
        #While the dialogue datatable contains lip movement information it is completely ignored by the game
        #So the only solution left is to rename the pointer of every lip file to match the random dialogue
        #Quite a bit costly but this is the only way
        for event in cls.event_replacement:
            cls._update_lip_pointer(event, cls.event_replacement[event])

    @classmethod
    def _update_lip_pointer(cls, old_event, new_event):
        #Simply swap the file's name in the name map and save as the new name
        old_event = f"{cls.voice_language}_{old_event}_LIP"
        new_event = f"{cls.voice_language}_{new_event}_LIP"
        
        if f"{new_event}.uasset" in os.listdir("Data\\LipSync"):
            new_event_data = UAsset(f"Data\\LipSync\\{new_event}.uasset", EngineVersion.VER_UE4_22)
            index = new_event_data.SearchNameReference(FString(new_event))
            new_event_data.SetNameReference(index, FString(old_event))
            index = new_event_data.SearchNameReference(FString(f"/Game/Core/UI/Dialog/Data/LipSync/{new_event}"))
            new_event_data.SetNameReference(index, FString(f"/Game/Core/UI/Dialog/Data/LipSync/{old_event}"))
            new_event_data.Write(f"{MOD_DIR}\\Core\\UI\\Dialog\\Data\\LipSync\\{old_event}.uasset")
        elif f"{old_event}.uasset" in os.listdir("Data\\LipSync"):
            old_event_data = UAsset(f"Data\\LipSync\\{old_event}.uasset", EngineVersion.VER_UE4_22)
            for export in old_event_data.Exports:
                if str(export.ObjectName) == old_event:
                    export.Data.Clear()
            old_event_data.Write(f"{MOD_DIR}\\Core\\UI\\Dialog\\Data\\LipSync\\{old_event}.uasset")

    @classmethod
    def add_music_file(cls, filename : str):
        #Check if the filename is valid
        matches = re.match(r'ACT([1-9]\d)_(...)', filename)
        if not matches:
            raise TypeError(f"Invalid music name: {filename}")
        digits, name_end = matches.groups()

        #Copy the awb and import the new music in it
        old_awb_name = ASSETS_DIR + "\\" + Data.file_to_path["ACT50_BRM"] + "\\ACT50_BRM.awb"
        new_awb_name = MOD_DIR + "\\" + Data.file_to_path["ACT50_BRM"] + "\\" + filename + ".awb"
        with open(old_awb_name, "rb") as inputfile, open(new_awb_name, "wb") as outfile:
            offset = inputfile.read().find(str.encode("HCA"))
            inputfile.seek(0)
            outfile.write(inputfile.read(offset))
            with open(f"Data\\Music\\{filename}.hca", "rb") as hca:
                outfile.write(hca.read())
            outfile.seek(0, os.SEEK_END)
            filesize = outfile.tell()
            outfile.seek(0x16)
            outfile.write(filesize.to_bytes(4, "little"))
        #Add the music pointer in soundmaster
        music_id = "BGM_m" + digits + name_end
        Data.datatable["PB_DT_SoundMaster"][music_id] = copy.deepcopy(Data.datatable["PB_DT_SoundMaster"]["BGM_m50BRM"])
        replacement = cls.music_replacement[music_id] if music_id in cls.music_replacement else music_id
        Data.datatable["PB_DT_SoundMaster"][music_id]["AssetPath"] = f"/Game/Core/Sound/bgm/{replacement}.{replacement}"
        #Copy the act file
        new_file = UAsset(ASSETS_DIR + "\\" + Data.file_to_path["ACT50_BRM"] + "\\ACT50_BRM.uasset", EngineVersion.VER_UE4_22)
        index = new_file.SearchNameReference(FString("ACT50_BRM"))
        new_file.SetNameReference(index, FString(filename))
        index = new_file.SearchNameReference(FString("/Game/Core/Sound/bgm/ACT50_BRM"))
        new_file.SetNameReference(index, FString("/Game/Core/Sound/bgm/" + filename))
        new_file.Exports[0].Data[0].Value = FString(filename)
        string = "{:02x}".format(int.from_bytes(str.encode(filename), "big"))
        for num in range(int(len(string)/2)):
            new_file.Exports[0].Extras[0x662 + num] = int(string[num*2] + string[num*2 + 1], 16)
            new_file.Exports[0].Extras[0xE82 + num] = int(string[num*2] + string[num*2 + 1], 16)
        string = "{:02x}".format(int.from_bytes(str.encode(music_id), "big"))
        for num in range(int(len(string)/2)):
            new_file.Exports[0].Extras[0x7E1 + num] = int(string[num*2] + string[num*2 + 1], 16)
        string = "{:08x}".format(filesize)
        count = 0
        for num in range(int(len(string)/2) -1, -1, -1):
            new_file.Exports[0].Extras[0x1A32 + count] = int(string[num*2] + string[num*2 + 1], 16)
            count += 1
        new_file.Write(MOD_DIR + "\\" + Data.file_to_path["ACT50_BRM"] + "\\" + filename + ".uasset")
        #Copy the bgm file
        new_file = UAsset(ASSETS_DIR + "\\" + Data.file_to_path["BGM_m50BRM"] + "\\BGM_m50BRM.uasset", EngineVersion.VER_UE4_22)
        index = new_file.SearchNameReference(FString("ACT50_BRM"))
        new_file.SetNameReference(index, FString(filename))
        index = new_file.SearchNameReference(FString("/Game/Core/Sound/bgm/ACT50_BRM"))
        new_file.SetNameReference(index, FString(f"/Game/Core/Sound/bgm/{filename}"))
        index = new_file.SearchNameReference(FString("BGM_m50BRM"))
        new_file.SetNameReference(index, FString(music_id))
        index = new_file.SearchNameReference(FString("/Game/Core/Sound/bgm/BGM_m50BRM"))
        new_file.SetNameReference(index, FString(f"/Game/Core/Sound/bgm/{music_id}"))
        new_file.Exports[0].Data[1].Value = FString(music_id)
        new_file.Exports[0].Data[2].Value = 300.0
        new_file.Write(MOD_DIR + "\\" + Data.file_to_path["BGM_m50BRM"] + "\\" + music_id + ".uasset")