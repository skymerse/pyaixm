from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeCommunicationModeBaseTypeValue(Enum):
    HF = "HF"
    VHF = "VHF"
    VDL1 = "VDL1"
    VDL2 = "VDL2"
    VDL4 = "VDL4"
    AMSS = "AMSS"
    ADS_B = "ADS_B"
    ADS_B_VDL = "ADS_B_VDL"
    HFDL = "HFDL"
    VHF_833 = "VHF_833"
    UHF = "UHF"
