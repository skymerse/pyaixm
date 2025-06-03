from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeApprovalBaseTypeValue(Enum):
    APPROVED = "APPROVED"
    DISAPPROVED = "DISAPPROVED"
    NOT_AUTHORISED = "NOT_AUTHORISED"
    RESTRICTED = "RESTRICTED"
