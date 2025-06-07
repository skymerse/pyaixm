from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class InterpretationValue(Enum):
    BASELINE = "BASELINE"
    SNAPSHOT = "SNAPSHOT"
    TEMPDELTA = "TEMPDELTA"
    PERMDELTA = "PERMDELTA"
