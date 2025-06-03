from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeMissedApproachBaseTypeValue(Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    ALTERNATE = "ALTERNATE"
    TACAN = "TACAN"
    TACANALT = "TACANALT"
    ENGINEOUT = "ENGINEOUT"
