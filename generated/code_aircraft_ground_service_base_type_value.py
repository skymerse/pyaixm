from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAircraftGroundServiceBaseTypeValue(Enum):
    DEICE = "DEICE"
    HAND = "HAND"
    HANGAR = "HANGAR"
    REPAIR = "REPAIR"
    REMOVE = "REMOVE"
