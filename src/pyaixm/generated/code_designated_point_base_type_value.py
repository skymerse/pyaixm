from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeDesignatedPointBaseTypeValue(Enum):
    ICAO = "ICAO"
    COORD = "COORD"
    CNF = "CNF"
    DESIGNED = "DESIGNED"
    MTR = "MTR"
    TERMINAL = "TERMINAL"
    BRG_DIST = "BRG_DIST"
