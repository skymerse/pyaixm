from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeMarkingStatusBaseType(Enum):
    OBSC = "OBSC"
    PART_OBSC = "PART_OBSC"
    FADED = "FADED"
    REMOVED = "REMOVED"
    NONE = "NONE"
    NON_STANDARD = "NON_STANDARD"
