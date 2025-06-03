from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodePassengerServiceBaseTypeValue(Enum):
    CUST = "CUST"
    SAN = "SAN"
    SECUR = "SECUR"
    VET = "VET"
    HOTEL = "HOTEL"
    TRANSPORT = "TRANSPORT"
    REST = "REST"
    INFO = "INFO"
    BANK = "BANK"
    POST = "POST"
    MEDIC = "MEDIC"
