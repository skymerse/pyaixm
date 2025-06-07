from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeLevelTableDesignatorBaseTypeValue(Enum):
    IFR = "IFR"
    IFR_METRES = "IFR_METRES"
    VFR = "VFR"
    VFR_METRES = "VFR_METRES"
    IFR_RVSM = "IFR_RVSM"
    IFR_METRES_RVSM = "IFR_METRES_RVSM"
    VFR_RVMS = "VFR_RVMS"
    VFR_METRES_RVSM = "VFR_METRES_RVSM"
