import os
import clr
import sys
import math
import random
import copy

sys.path.append(os.path.abspath("Tools\\UAssetAPI"))
clr.AddReference("UAssetAPI") # type: ignore
clr.AddReference("UAssetSnippet") # type: ignore

from UAssetAPI import *
from UAssetAPI.ExportTypes import *
from UAssetAPI.FieldTypes import *
from UAssetAPI.JSON import *
from UAssetAPI.Kismet import *
from UAssetAPI.Kismet.Bytecode import *
from UAssetAPI.Kismet.Bytecode.Expressions import *
from UAssetAPI.PropertyTypes import *
from UAssetAPI.PropertyTypes.Objects import *
from UAssetAPI.PropertyTypes.Structs import *
from UAssetAPI.UnrealTypes import *
from UAssetAPI.Unversioned import *
from UAssetSnippet import *
