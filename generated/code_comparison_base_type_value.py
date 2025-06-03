from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeComparisonBaseTypeValue(Enum):
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    EQUAL = "EQUAL"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    GREATER = "GREATER"
