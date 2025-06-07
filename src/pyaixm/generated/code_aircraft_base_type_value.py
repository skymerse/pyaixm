from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeAircraftBaseTypeValue(Enum):
    LANDPLANE = "LANDPLANE"
    SEAPLANE = "SEAPLANE"
    AMPHIBIAN = "AMPHIBIAN"
    HELICOPTER = "HELICOPTER"
    GYROCOPTER = "GYROCOPTER"
    TILT_WING = "TILT_WING"
    STOL = "STOL"
    GLIDER = "GLIDER"
    HANGGLIDER = "HANGGLIDER"
    PARAGLIDER = "PARAGLIDER"
    ULTRA_LIGHT = "ULTRA_LIGHT"
    BALLOON = "BALLOON"
    UAV = "UAV"
    ALL = "ALL"
