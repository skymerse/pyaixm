from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFrictionEstimateBaseTypeValue(Enum):
    GOOD = "GOOD"
    MEDIUM_GOOD = "MEDIUM_GOOD"
    MEDIUM = "MEDIUM"
    MEDIUM_POOR = "MEDIUM_POOR"
    POOR = "POOR"
    UNRELIABLE = "UNRELIABLE"
