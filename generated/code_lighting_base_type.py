from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeLightingBaseType(Enum):
    TDZL = "TDZL"
    RCLL = "RCLL"
    EDGE = "EDGE"
    THR = "THR"
    REIL = "REIL"
    TLOF = "TLOF"
    LEAD_ON = "LEAD_ON"
    LAHSO = "LAHSO"
    FAROS = "FAROS"
    RLLS = "RLLS"
    RWSL = "RWSL"
    REL = "REL"
    THL = "THL"
    LIRL = "LIRL"
    MIRL = "MIRL"
    HIRL = "HIRL"
    ALS = "ALS"
