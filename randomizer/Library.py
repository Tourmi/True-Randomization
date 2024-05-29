from .GlobalImports import *
from .requirement_curve import get_curve
from . import Data
from . import Utility

class Library:
    @classmethod
    def init(cls):
        cls.tome_to_properties : dict[str, tuple[int, bool]] = {}

    @classmethod
    def set_requirement_weight(cls, weight : int):
        cls.requirement_curve = get_curve(weight-1)

    @classmethod
    def randomize_library_requirements(cls):
        #Fill requirement list
        property_list : list[tuple[int, bool]] = []
        for num in range(20):
            completion = cls.requirement_curve(num)
            property_list.append((completion, num % 2 == 0))
        property_list.append((99, True))
        #Assign tome of conquest
        chosen = random.choice(property_list)
        while not chosen[1]:
            chosen = random.choice(property_list)
        property_list.remove(chosen)
        cls.tome_to_properties["Bookofthechampion"] = chosen
        Data.datatable["PB_DT_BookMaster"]["Bookofthechampion"]["RoomTraverseThreshold"] = chosen[0]
        #Assign the rest
        for entry in Data.datatable["PB_DT_BookMaster"]:
            if entry in ["Dummy", "Bookofthechampion"]:
                continue
            cls.tome_to_properties[entry] = Utility.pick_and_remove(property_list)
            Data.datatable["PB_DT_BookMaster"][entry]["RoomTraverseThreshold"] = cls.tome_to_properties[entry][0]

    @classmethod
    def randomize_tome_appearance(cls):
        #If requirements were randomized remove tomes that have uneven indexes
        if cls.tome_to_properties:
            for entry in Data.datatable["PB_DT_BookMaster"]:
                if entry in ["Dummy", "Bookofthechampion"]:
                    continue
                Data.datatable["PB_DT_BookMaster"][entry]["IslibraryBook"] = cls.tome_to_properties[entry][1]
        #If requirements are vanilla remove 10 tomes at complete random
        else:
            book_list = list(Data.datatable["PB_DT_BookMaster"])
            book_list.remove("Dummy")
            book_list.remove("Bookofthechampion")
            for num in range(10):
                chosen = Utility.pick_and_remove(book_list)
                Data.datatable["PB_DT_BookMaster"][chosen]["IslibraryBook"] = False

    @staticmethod
    def create_log():
        log = {}
        for entry in Data.datatable["PB_DT_BookMaster"]:
            if Data.datatable["PB_DT_BookMaster"][entry]["IslibraryBook"]:
                log[Data.translation["Item"][entry]] = Data.datatable["PB_DT_BookMaster"][entry]["RoomTraverseThreshold"]
        return log