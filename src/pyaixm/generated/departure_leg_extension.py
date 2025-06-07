from dataclasses import dataclass

from generated.departure_leg_extension_type import DepartureLegExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DepartureLegExtension(DepartureLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
