import os
import sys

SCRIPT_NAME = os.path.splitext(os.path.basename(sys.argv[0]))[0]
UPDATE_URL = "https://api.github.com/repos/Lakifume/True-Randomization/releases/latest"
MOD_DIR = "Tools\\UnrealPak\\Mod\\BloodstainedRotN\\Content"
ASSETS_DIR = "Game"

WEIGHT_EXPONENTS : list[float] = [3, 1.8, 1.25]

KEY_ITEMS = [
    "Swordsman",
    "Silverbromide",
    "BreastplateofAguilar",
    "Keyofbacker1",
    "Keyofbacker2",
    "Keyofbacker3",
    "Keyofbacker4",
    "MonarchCrown"
]