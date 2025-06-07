from dataclasses import dataclass

from pyaixm.generated.callsign_detail_type import CallsignDetailType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CallsignDetail(CallsignDetailType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
