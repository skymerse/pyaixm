from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRunwayMarkingBaseTypeValue(Enum):
    PRECISION = "PRECISION"
    NONPRECISION = "NONPRECISION"
    BASIC = "BASIC"
    NONE = "NONE"
    RUNWAY_NUMBERS = "RUNWAY_NUMBERS"
    NON_STANDARD = "NON_STANDARD"
    HELIPORT = "HELIPORT"
