from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAircraftEngineBaseTypeValue(Enum):
    JET = "JET"
    PISTON = "PISTON"
    TURBOPROP = "TURBOPROP"
    ALL = "ALL"
