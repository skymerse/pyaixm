from dataclasses import dataclass

from generated.callsign_detail_type import CallsignDetailType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CallsignDetail(CallsignDetailType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
