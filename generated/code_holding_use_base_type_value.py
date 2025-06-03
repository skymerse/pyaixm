from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeHoldingUseBaseTypeValue(Enum):
    PT = "PT"
    ARRIVAL = "ARRIVAL"
    MISSED_APPROACH = "MISSED_APPROACH"
    CLIMB = "CLIMB"
    ATC = "ATC"
