from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRunwaySectionBaseTypeValue(Enum):
    TDZ = "TDZ"
    AIM = "AIM"
    CL = "CL"
    EDGE = "EDGE"
    THR = "THR"
    DESIG = "DESIG"
    AFT_THR = "AFT_THR"
    DTHR = "DTHR"
    END = "END"
    TWY_INT = "TWY_INT"
    RPD_TWY_INT = "RPD_TWY_INT"
    VALUE_1_THIRD = "1_THIRD"
    VALUE_2_THIRD = "2_THIRD"
    VALUE_3_THIRD = "3_THIRD"
