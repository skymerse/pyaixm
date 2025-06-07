from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeApronElementBaseTypeValue(Enum):
    NORMAL = "NORMAL"
    PARKING = "PARKING"
    RAMP = "RAMP"
    CARGO = "CARGO"
    FUEL = "FUEL"
    HARDSTAND = "HARDSTAND"
    MAINT = "MAINT"
    MILITARY = "MILITARY"
    LOADING = "LOADING"
    TAXILANE = "TAXILANE"
    TURNAROUND = "TURNAROUND"
    TEMPORARY = "TEMPORARY"
    STAIRS = "STAIRS"
