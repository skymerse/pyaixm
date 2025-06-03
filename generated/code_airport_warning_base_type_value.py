from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAirportWarningBaseTypeValue(Enum):
    WIP = "WIP"
    EQUIP = "EQUIP"
    BIRD = "BIRD"
    ANIMAL = "ANIMAL"
    RUBBER_REMOVAL = "RUBBER_REMOVAL"
    PARKED_ACFT = "PARKED_ACFT"
    RESURFACING = "RESURFACING"
    PAVING = "PAVING"
    PAINTING = "PAINTING"
    INSPECTION = "INSPECTION"
    GRASS_CUTTING = "GRASS_CUTTING"
    CALIBRATION = "CALIBRATION"
