from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeFlightRestrictionBaseTypeValue(Enum):
    FORBID = "FORBID"
    MANDATORY = "MANDATORY"
    CLSD = "CLSD"
    ALLOWED = "ALLOWED"
