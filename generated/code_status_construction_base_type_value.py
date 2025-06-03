from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeStatusConstructionBaseTypeValue(Enum):
    IN_CONSTRUCTION = "IN_CONSTRUCTION"
    COMPLETED = "COMPLETED"
    DEMOLITION_PLANNED = "DEMOLITION_PLANNED"
    IN_DEMOLITION = "IN_DEMOLITION "
