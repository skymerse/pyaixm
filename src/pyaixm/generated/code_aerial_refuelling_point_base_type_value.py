from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAerialRefuellingPointBaseTypeValue(Enum):
    INITIAL = "INITIAL"
    CONTROL = "CONTROL"
    CHECK = "CHECK"
    EXIT = "EXIT"
    ENTRY = "ENTRY"
    ANCHOR = "ANCHOR"
    PATTERN = "PATTERN"
