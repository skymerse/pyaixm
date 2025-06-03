from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeSegmentTerminationBaseTypeValue(Enum):
    ALTITUDE = "ALTITUDE"
    DISTANCE = "DISTANCE"
    DURATION = "DURATION"
    INTERCEPT = "INTERCEPT"
