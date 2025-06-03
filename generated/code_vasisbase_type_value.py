from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeVasisbaseTypeValue(Enum):
    PAPI = "PAPI"
    APAPI = "APAPI"
    HAPI = "HAPI"
    VASIS = "VASIS"
    AVASIS = "AVASIS"
    TVASIS = "TVASIS"
    ATVASIS = "ATVASIS"
    VALUE_3_B_VASIS = "3B_VASIS"
    VALUE_3_B_AVASIS = "3B_AVASIS"
    VALUE_3_B_ATVASIS = "3B_ATVASIS"
    PVASI = "PVASI"
    TRCV = "TRCV"
    PNI = "PNI"
    ILU = "ILU"
    OLS = "OLS"
    LCVASI = "LCVASI"
