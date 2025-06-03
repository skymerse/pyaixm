from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlightPurposeBaseTypeValue(Enum):
    SCHEDULED = "SCHEDULED"
    NON_SCHEDULED = "NON_SCHEDULED"
    PRIVATE = "PRIVATE"
    AIR_TRAINING = "AIR_TRAINING"
    AIR_WORK = "AIR_WORK"
    ALL = "ALL"
    PARTICIPANT = "PARTICIPANT"
