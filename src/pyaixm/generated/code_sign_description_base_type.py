from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeSignDescriptionBaseType(Enum):
    ALL = "ALL"
    OUTBOUND = "OUTBOUND"
    INBOUND = "INBOUND"
