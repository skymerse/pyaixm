from dataclasses import dataclass

from generated.traffic_separation_service_extension_type import (
    TrafficSeparationServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TrafficSeparationServiceExtension(TrafficSeparationServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
