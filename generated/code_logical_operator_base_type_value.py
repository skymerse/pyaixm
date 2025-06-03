from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeLogicalOperatorBaseTypeValue(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    NONE = "NONE"
