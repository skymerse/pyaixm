from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeProcedurePhaseBaseTypeValue(Enum):
    RWY = "RWY"
    COMMON = "COMMON"
    EN_ROUTE = "EN_ROUTE"
    APPROACH = "APPROACH"
    FINAL = "FINAL"
    MISSED = "MISSED"
    MISSED_P = "MISSED_P"
    MISSED_S = "MISSED_S"
    ENGINE_OUT = "ENGINE_OUT"
