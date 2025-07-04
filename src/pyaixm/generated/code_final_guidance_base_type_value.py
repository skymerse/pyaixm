from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFinalGuidanceBaseTypeValue(Enum):
    LPV = "LPV"
    LNAV_VNAV = "LNAV_VNAV"
    LNAV = "LNAV"
    GLS = "GLS"
    ASR = "ASR"
    ARA = "ARA"
    ARSR = "ARSR"
    PAR = "PAR"
    ILS = "ILS"
    ILS_DME = "ILS_DME"
    ILS_PRM = "ILS_PRM"
    LDA = "LDA"
    LDA_DME = "LDA_DME"
    LOC = "LOC"
    LOC_BC = "LOC_BC"
    LOC_DME = "LOC_DME"
    LOC_DME_BC = "LOC_DME_BC"
    MLS = "MLS"
    MLS_DME = "MLS_DME"
    NDB = "NDB"
    NDB_DME = "NDB_DME"
    SDF = "SDF"
    TLS = "TLS"
    VOR = "VOR"
    VOR_DME = "VOR_DME"
    TACAN = "TACAN"
    VORTAC = "VORTAC"
    DME = "DME"
    LP = "LP"
