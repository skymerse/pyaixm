from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeCourseBaseTypeValue(Enum):
    TRUE_TRACK = "TRUE_TRACK"
    MAG_TRACK = "MAG_TRACK"
    TRUE_BRG = "TRUE_BRG"
    MAG_BRG = "MAG_BRG"
    HDG = "HDG"
    RDL = "RDL"
