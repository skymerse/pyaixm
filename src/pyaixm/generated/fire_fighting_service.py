from dataclasses import dataclass

from generated.fire_fighting_service_type import FireFightingServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FireFightingService(FireFightingServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
