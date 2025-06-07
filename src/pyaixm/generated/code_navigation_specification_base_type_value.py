from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeNavigationSpecificationBaseTypeValue(Enum):
    RNAV_10 = "RNAV_10"
    RNAV_5 = "RNAV_5"
    RNAV_2 = "RNAV_2"
    RNAV_1 = "RNAV_1"
    RNP_4 = "RNP_4"
    RNP_2 = "RNP_2"
    BASIC_RNP_1 = "BASIC_RNP_1"
    ADVANCED_RNP_1 = "ADVANCED_RNP_1"
    RNP_APCH = "RNP_APCH"
    RNP_AR_APCH = "RNP_AR_APCH"
