from enum import Enum

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


class CodeResponseStatusBaseType(Enum):
    OK = "OK"
    DATA_MISSING_ERROR = "DATA_MISSING_ERROR"
    USER_LOGIN_ERROR = "USER_LOGIN_ERROR"
    DATA_VALIDATION_ERROR = "DATA_VALIDATION_ERROR"
    SYSTEM_ERROR = "SYSTEM_ERROR"
