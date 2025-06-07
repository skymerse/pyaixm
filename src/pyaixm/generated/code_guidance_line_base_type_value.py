from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeGuidanceLineBaseTypeValue(Enum):
    RWY = "RWY"
    TWY = "TWY"
    APRON = "APRON"
    GATE_TLANE = "GATE_TLANE"
    LI_TLANE = "LI_TLANE"
    LO_TLANE = "LO_TLANE"
    AIR_TLANE = "AIR_TLANE"
