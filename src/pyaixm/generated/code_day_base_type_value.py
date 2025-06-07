from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeDayBaseTypeValue(Enum):
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
    WORK_DAY = "WORK_DAY"
    BEF_WORK_DAY = "BEF_WORK_DAY"
    AFT_WORK_DAY = "AFT_WORK_DAY"
    HOL = "HOL"
    BEF_HOL = "BEF_HOL"
    AFT_HOL = "AFT_HOL"
    ANY = "ANY"
    BUSY_FRI = "BUSY_FRI"
