from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeApproachLightingIcaobaseTypeValue(Enum):
    SIMPLE = "SIMPLE"
    CAT1 = "CAT1"
    CAT23 = "CAT23"
    CIRCLING = "CIRCLING"
    LEADIN = "LEADIN"
    NONE = "NONE"
