from .GlobalImports import *
from .Constants import *
from . import Data
from . import Utility

class Shop:
    PRICE_SKIP_LIST = [
        "Potion",
        "Ether",
        "Waystone"
    ]

    @classmethod
    def set_shop_price_weight(cls, weight : int):
        cls.shop_price_weight = WEIGHT_EXPONENTS[weight - 1]

    @classmethod
    def randomize_shop_prices(cls, scale : bool):
        for entry in Data.datatable["PB_DT_ItemMaster"]:
            if Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"] == 0 or entry in cls.PRICE_SKIP_LIST:
                continue
            #Buy
            buy_price = Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"]
            sell_ratio = Data.datatable["PB_DT_ItemMaster"][entry]["sellPrice"]/buy_price
            multiplier = Utility.random_weighted(1.0, 0.01, 100.0, 0.01, cls.shop_price_weight, False)
            Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"] = int(buy_price*multiplier)
            Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"] = max(Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"], 1)
            if Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"] > 10:
                Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"] = round(Data.datatable["PB_DT_ItemMaster"][entry]["buyPrice"]/10)*10
            #Sell
            if not scale:
                multiplier = Utility.random_weighted(1.0, 0.01, 100.0, 0.01, cls.shop_price_weight, False)
            Data.datatable["PB_DT_ItemMaster"][entry]["sellPrice"] = int(buy_price*multiplier*sell_ratio)
            Data.datatable["PB_DT_ItemMaster"][entry]["sellPrice"] = max(Data.datatable["PB_DT_ItemMaster"][entry]["sellPrice"], 1)
