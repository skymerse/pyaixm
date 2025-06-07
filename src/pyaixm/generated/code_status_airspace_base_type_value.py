from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeStatusAirspaceBaseTypeValue(Enum):
    AVBL_FOR_ACTIVATION = "AVBL_FOR_ACTIVATION"
    ACTIVE = "ACTIVE"
    IN_USE = "IN_USE"
    INACTIVE = "INACTIVE"
    INTERMITTENT = "INTERMITTENT"
