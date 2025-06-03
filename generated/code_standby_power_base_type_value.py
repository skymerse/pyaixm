from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeStandbyPowerBaseTypeValue(Enum):
    BATTERY = "BATTERY"
    COMMERCIAL = "COMMERCIAL"
    GENERATOR = "GENERATOR"
    UNKNOWN = "UNKNOWN"
    NONE = "NONE"
