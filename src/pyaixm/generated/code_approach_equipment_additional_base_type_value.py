from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeApproachEquipmentAdditionalBaseTypeValue(Enum):
    ADF = "ADF"
    DME = "DME"
    RADAR = "RADAR"
    RADARDME = "RADARDME"
    VORLOC = "VORLOC"
    DUALVORDME = "DUALVORDME"
    DUALADF = "DUALADF"
    ADFMA = "ADFMA"
    SPECIAL = "SPECIAL"
    DUALVHF = "DUALVHF"
    GPSRNP3 = "GPSRNP3"
    ADFILS = "ADFILS"
    DUALADF_DME = "DUALADF_DME"
    RADAR_RNAV = "RADAR_RNAV"
