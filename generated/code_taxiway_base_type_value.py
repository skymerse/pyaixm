from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeTaxiwayBaseTypeValue(Enum):
    AIR = "AIR"
    GND = "GND"
    EXIT = "EXIT"
    FASTEXIT = "FASTEXIT"
    STUB = "STUB"
    TURN_AROUND = "TURN_AROUND"
    PARALLEL = "PARALLEL"
    BYPASS = "BYPASS"
