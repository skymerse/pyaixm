from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFacilityRankingBaseTypeValue(Enum):
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    ALTERNATE = "ALTERNATE"
    EMERG = "EMERG"
    GUARD = "GUARD"
