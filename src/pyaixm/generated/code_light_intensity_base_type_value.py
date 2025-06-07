from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeLightIntensityBaseTypeValue(Enum):
    LIL = "LIL"
    LIM = "LIM"
    LIH = "LIH"
    LIL_LIH = "LIL_LIH"
    PREDETERMINED = "PREDETERMINED"
