from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeSignStatusBaseType(Enum):
    UNLIGHTED = "UNLIGHTED"
    OBSCURED = "OBSCURED"
    UNSERVICEABLE = "UNSERVICEABLE"
    NON_STANDARD = "NON_STANDARD"
