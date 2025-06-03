from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAirspaceAggregationBaseTypeValue(Enum):
    BASE = "BASE"
    UNION = "UNION"
    INTERS = "INTERS"
    SUBTR = "SUBTR"
