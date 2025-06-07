from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeProcedureDistanceBaseTypeValue(Enum):
    HAT = "HAT"
    OM = "OM"
    MM = "MM"
    IM = "IM"
    PFAF = "PFAF"
    GSANT = "GSANT"
    FAF = "FAF"
    MAP = "MAP"
    THLD = "THLD"
    VDP = "VDP"
    RECH = "RECH"
