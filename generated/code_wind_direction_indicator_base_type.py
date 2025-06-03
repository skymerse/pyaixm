from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeWindDirectionIndicatorBaseType(Enum):
    WINDCONE = "WINDCONE"
    TETRAHEDRON = "TETRAHEDRON"
    WIND_TEE = "WIND_TEE"
