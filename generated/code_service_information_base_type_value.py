from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeServiceInformationBaseTypeValue(Enum):
    AFIS = "AFIS"
    AIS = "AIS"
    ATIS = "ATIS"
    BRIEFING = "BRIEFING"
    FIS = "FIS"
    OFIS_VHF = "OFIS_VHF"
    OFIS_HF = "OFIS_HF"
    NOTAM = "NOTAM"
    INFO = "INFO"
    RAF = "RAF"
    METAR = "METAR"
    SIGMET = "SIGMET"
    TWEB = "TWEB"
    TAF = "TAF"
    VOLMET = "VOLMET"
    ALTIMETER = "ALTIMETER"
    ASOS = "ASOS"
    AWOS = "AWOS"
