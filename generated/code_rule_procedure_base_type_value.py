from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRuleProcedureBaseTypeValue(Enum):
    RULE = "RULE"
    LAW = "LAW"
    PROCEDURE = "PROCEDURE"
    PRACTICE = "PRACTICE"
    ICAO_DIFF = "ICAO_DIFF"
