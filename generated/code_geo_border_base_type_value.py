from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeGeoBorderBaseTypeValue(Enum):
    STATE = "STATE"
    WATER = "WATER"
    COAST = "COAST"
    RIVER = "RIVER"
    BANK = "BANK"
