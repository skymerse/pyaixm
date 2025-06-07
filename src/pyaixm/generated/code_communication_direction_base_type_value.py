from enum import Enum

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


class CodeCommunicationDirectionBaseTypeValue(Enum):
    UPLINK = "UPLINK"
    DOWNLINK = "DOWNLINK"
    BIDIRECTIONAL = "BIDIRECTIONAL"
    UPCAST = "UPCAST"
    DOWNCAST = "DOWNCAST"
