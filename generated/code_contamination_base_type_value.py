from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeContaminationBaseTypeValue(Enum):
    NONE = "NONE"
    DAMP = "DAMP"
    WATER = "WATER"
    FROST = "FROST"
    DRY_SNOW = "DRY_SNOW"
    WET_SNOW = "WET_SNOW"
    SLUSH = "SLUSH"
    ICE = "ICE"
    COMPACT_SNOW = "COMPACT_SNOW"
    RUT = "RUT"
    ASH = "ASH"
    SAND = "SAND"
    OIL = "OIL"
    RUBBER = "RUBBER"
    GRAS = "GRAS"
