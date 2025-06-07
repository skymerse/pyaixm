from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeOrganisationBaseTypeValue(Enum):
    STATE = "STATE"
    STATE_GROUP = "STATE_GROUP"
    ORG = "ORG"
    INTL_ORG = "INTL_ORG"
    ACFT_OPR = "ACFT_OPR"
    HANDLING_AGENCY = "HANDLING_AGENCY"
    NTL_AUTH = "NTL_AUTH"
    ATS = "ATS"
    COMMERCIAL = "COMMERCIAL"
