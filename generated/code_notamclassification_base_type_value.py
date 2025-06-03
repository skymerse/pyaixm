from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE"


class CodeNotamclassificationBaseTypeValue(Enum):
    INTL = "INTL"
    DOM = "DOM"
    MIL = "MIL"
    LMIL = "LMIL"
    FDC = "FDC"
