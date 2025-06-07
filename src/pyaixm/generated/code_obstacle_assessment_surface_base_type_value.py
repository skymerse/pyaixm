from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeObstacleAssessmentSurfaceBaseTypeValue(Enum):
    VALUE_40_TO_1 = "40_TO_1"
    VALUE_72_TO_1 = "72_TO_1"
    MA = "MA"
    FINAL = "FINAL"
    PT_ENTRY_AREA = "PT_ENTRY_AREA"
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    ZONE1 = "ZONE1"
    ZONE2 = "ZONE2"
    ZONE3 = "ZONE3"
    AREA1 = "AREA1"
    AREA2 = "AREA2"
    AREA3 = "AREA3"
    TURN_INITIATION = "TURN_INITIATION"
    TURN = "TURN"
    DER = "DER"
