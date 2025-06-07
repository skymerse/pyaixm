from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeTaxiwayMarkingBaseType(Enum):
    SHOULDER = "SHOULDER"
    DIRECTION = "DIRECTION"
    LOCATION = "LOCATION"
    GEOGRAPHIC_POS = "GEOGRAPHIC_POS"
