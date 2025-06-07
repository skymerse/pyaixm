from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeUsageLimitationBaseTypeValue(Enum):
    PERMIT = "PERMIT"
    CONDITIONAL = "CONDITIONAL"
    FORBID = "FORBID"
    RESERV = "RESERV"
