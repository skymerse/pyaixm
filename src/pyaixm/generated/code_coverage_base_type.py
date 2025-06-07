from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeCoverageBaseType(Enum):
    PATCHY = "PATCHY"
    FULLY_COVERED = "FULLY_COVERED"
