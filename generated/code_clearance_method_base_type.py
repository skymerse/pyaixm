from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeClearanceMethodBaseType(Enum):
    PLOWED = "PLOWED"
    SANDED = "SANDED"
    SWEPT = "SWEPT"
    PLOWED_SWEPT = "PLOWED_SWEPT"
    PLOWED_SWEPT_SANDED = "PLOWED_SWEPT_SANDED"
    DEICED_LIQUID = "DEICED_LIQUID"
    DEICED_SOLID = "DEICED_SOLID"
