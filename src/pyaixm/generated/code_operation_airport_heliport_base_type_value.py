from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeOperationAirportHeliportBaseTypeValue(Enum):
    LANDING = "LANDING"
    TAKEOFF = "TAKEOFF"
    TOUCHGO = "TOUCHGO"
    TRAIN_APPROACH = "TRAIN_APPROACH"
    ALTN_LANDING = "ALTN_LANDING"
    AIRSHOW = "AIRSHOW"
    ALL = "ALL"
