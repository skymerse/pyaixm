from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlightRuleBaseTypeValue(Enum):
    IFR = "IFR"
    VFR = "VFR"
    ALL = "ALL"
