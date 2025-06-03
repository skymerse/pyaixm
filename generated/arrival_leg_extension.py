from dataclasses import dataclass

from generated.arrival_leg_extension_type import ArrivalLegExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ArrivalLegExtension(ArrivalLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
