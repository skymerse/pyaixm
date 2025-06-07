from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class UomSpeedTypeValue(Enum):
    KM_H = "KM_H"
    KT = "KT"
    MACH = "MACH"
    M_MIN = "M_MIN"
    FT_MIN = "FT_MIN"
    M_SEC = "M_SEC"
    FT_SEC = "FT_SEC"
    MPH = "MPH"
