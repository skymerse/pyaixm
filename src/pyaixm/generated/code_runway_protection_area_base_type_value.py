from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRunwayProtectionAreaBaseTypeValue(Enum):
    CWY = "CWY"
    RESA = "RESA"
    OFZ = "OFZ"
    IOFZ = "IOFZ"
    POFZ = "POFZ"
    ILS = "ILS"
    VGSI = "VGSI"
    STOPWAY = "STOPWAY"
