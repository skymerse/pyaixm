from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeSurfaceConditionBaseTypeValue(Enum):
    GOOD = "GOOD"
    FAIR = "FAIR"
    POOR = "POOR"
    UNSAFE = "UNSAFE"
    DEFORMED = "DEFORMED"
