from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlowConditionOperationBaseTypeValue(Enum):
    AND = "AND"
    ANDNOT = "ANDNOT"
    OR = "OR"
    SEQ = "SEQ"
    NONE = "NONE"
