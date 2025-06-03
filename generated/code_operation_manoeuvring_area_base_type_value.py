from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeOperationManoeuvringAreaBaseTypeValue(Enum):
    LANDING = "LANDING"
    TAKEOFF = "TAKEOFF"
    TOUCHGO = "TOUCHGO"
    TRAIN_APPROACH = "TRAIN_APPROACH"
    TAXIING = "TAXIING"
    CROSSING = "CROSSING"
    AIRSHOW = "AIRSHOW"
    ALL = "ALL"
