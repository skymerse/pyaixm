from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeBearingBaseTypeValue(Enum):
    TRUE = "TRUE"
    MAG = "MAG"
    RDL = "RDL"
    TRK = "TRK"
    HDG = "HDG"
