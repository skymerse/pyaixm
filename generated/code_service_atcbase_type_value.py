from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeServiceAtcbaseTypeValue(Enum):
    ACS = "ACS"
    UAC = "UAC"
    OACS = "OACS"
    APP = "APP"
    TWR = "TWR"
    ADVS = "ADVS"
    EFAS = "EFAS"
    CTAF = "CTAF"
