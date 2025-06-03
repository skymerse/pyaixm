from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeRadioSignalBaseTypeValue(Enum):
    AZIMUTH = "AZIMUTH"
    DISTANCE = "DISTANCE"
    BEAM = "BEAM"
    VOICE = "VOICE"
    DATALINK = "DATALINK"
