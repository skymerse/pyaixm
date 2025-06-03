from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeGroundLightingBaseTypeValue(Enum):
    BCN = "BCN"
    IBN = "IBN"
    HEL_BCN = "HEL_BCN"
    ABN = "ABN"
    MAR_BCN = "MAR_BCN"
    RSP_BCN = "RSP_BCN"
    TWR_BCN = "TWR_BCN"
    HAZ_BCN = "HAZ_BCN"
