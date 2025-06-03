from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlightStatusBaseTypeValue(Enum):
    HEAD = "HEAD"
    STATE = "STATE"
    HUM = "HUM"
    HOSP = "HOSP"
    SAR = "SAR"
    ALL = "ALL"
    EMERGENCY = "EMERGENCY"
