from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeBarrierBaseType(Enum):
    NONE = "NONE"
    BARRIER = "BARRIER"
    LIGHTED_BARRIER = "LIGHTED_BARRIER"
