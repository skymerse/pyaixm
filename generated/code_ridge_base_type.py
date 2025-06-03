from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeRidgeBaseType(Enum):
    DRIFT = "DRIFT"
    SNOWBANK = "SNOWBANK"
    BERM = "BERM"
