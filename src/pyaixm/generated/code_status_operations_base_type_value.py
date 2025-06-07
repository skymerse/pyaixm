from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeStatusOperationsBaseTypeValue(Enum):
    NORMAL = "NORMAL"
    DOWNGRADED = "DOWNGRADED"
    UNSERVICEABLE = "UNSERVICEABLE"
    WORK_IN_PROGRESS = "WORK_IN_PROGRESS"
