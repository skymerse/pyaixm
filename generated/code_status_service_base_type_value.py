from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeStatusServiceBaseTypeValue(Enum):
    NORMAL = "NORMAL"
    LIMITED = "LIMITED"
    ONTEST = "ONTEST"
    UNSERVICEABLE = "UNSERVICEABLE"
