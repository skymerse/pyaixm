from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAirportHeliportCollocationBaseTypeValue(Enum):
    FULL = "FULL"
    RWY = "RWY"
    PARTIAL = "PARTIAL"
    UNILATERAL = "UNILATERAL"
    SEPARATED = "SEPARATED"
