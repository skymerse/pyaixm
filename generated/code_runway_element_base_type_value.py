from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRunwayElementBaseTypeValue(Enum):
    NORMAL = "NORMAL"
    INTERSECTION = "INTERSECTION"
    DISPLACED = "DISPLACED"
    SHOULDER = "SHOULDER"
