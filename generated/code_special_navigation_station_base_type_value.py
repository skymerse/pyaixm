from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeSpecialNavigationStationBaseTypeValue(Enum):
    MASTER = "MASTER"
    SLAVE = "SLAVE"
    RED_SLAVE = "RED_SLAVE"
    GREEN_SLAVE = "GREEN_SLAVE"
    PURPLE_SLAVE = "PURPLE_SLAVE"
