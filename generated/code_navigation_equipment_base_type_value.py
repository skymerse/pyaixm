from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeNavigationEquipmentBaseTypeValue(Enum):
    DME = "DME"
    VOR_DME = "VOR_DME"
    DME_DME = "DME_DME"
    TACAN = "TACAN"
    ILS = "ILS"
    MLS = "MLS"
    GNSS = "GNSS"
    WAAS = "WAAS"
    LORAN = "LORAN"
    INS = "INS"
    FMS = "FMS"
