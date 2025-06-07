from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeNavaidServiceBaseTypeValue(Enum):
    VOR = "VOR"
    DME = "DME"
    NDB = "NDB"
    TACAN = "TACAN"
    MKR = "MKR"
    ILS = "ILS"
    ILS_DME = "ILS_DME"
    MLS = "MLS"
    MLS_DME = "MLS_DME"
    VORTAC = "VORTAC"
    VOR_DME = "VOR_DME"
    NDB_DME = "NDB_DME"
    TLS = "TLS"
    LOC = "LOC"
    LOC_DME = "LOC_DME"
    NDB_MKR = "NDB_MKR"
    DF = "DF"
    SDF = "SDF"
