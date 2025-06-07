from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAltitudeUseBaseTypeValue(Enum):
    ABOVE_LOWER = "ABOVE_LOWER"
    BELOW_UPPER = "BELOW_UPPER"
    AT_LOWER = "AT_LOWER"
    BETWEEN = "BETWEEN"
    RECOMMENDED = "RECOMMENDED"
    EXPECT_LOWER = "EXPECT_LOWER"
    AS_ASSIGNED = "AS_ASSIGNED"
