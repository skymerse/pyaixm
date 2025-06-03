from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeSurfacePreparationBaseTypeValue(Enum):
    NATURAL = "NATURAL"
    ROLLED = "ROLLED"
    COMPACTED = "COMPACTED"
    GRADED = "GRADED"
    GROOVED = "GROOVED"
    OILED = "OILED"
    PAVED = "PAVED"
    PFC = "PFC"
    AFSC = "AFSC"
    RFSC = "RFSC"
    NON_GROOVED = "NON_GROOVED"
