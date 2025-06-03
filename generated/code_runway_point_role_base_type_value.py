from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRunwayPointRoleBaseTypeValue(Enum):
    START = "START"
    THR = "THR"
    DISTHR = "DISTHR"
    TDZ = "TDZ"
    MID = "MID"
    END = "END"
    START_RUN = "START_RUN"
    LAHSO = "LAHSO"
    ABEAM_GLIDESLOPE = "ABEAM_GLIDESLOPE"
    ABEAM_PAR = "ABEAM_PAR"
    ABEAM_ELEVATION = "ABEAM_ELEVATION"
    ABEAM_TDR = "ABEAM_TDR"
    ABEAM_RER = "ABEAM_RER"
