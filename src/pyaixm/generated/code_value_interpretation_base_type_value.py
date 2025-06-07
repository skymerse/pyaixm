from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeValueInterpretationBaseTypeValue(Enum):
    ABOVE = "ABOVE"
    AT_OR_ABOVE = "AT_OR_ABOVE"
    AT_OR_BELOW = "AT_OR_BELOW"
    BELOW = "BELOW"
