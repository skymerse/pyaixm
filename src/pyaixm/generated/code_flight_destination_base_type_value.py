from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlightDestinationBaseTypeValue(Enum):
    ARR = "ARR"
    DEP = "DEP"
    OVERFLY = "OVERFLY"
    ALL = "ALL"
