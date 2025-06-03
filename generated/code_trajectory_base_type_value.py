from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeTrajectoryBaseTypeValue(Enum):
    STRAIGHT = "STRAIGHT"
    ARC = "ARC"
    PT = "PT"
    BASETURN = "BASETURN"
    HOLDING = "HOLDING"
