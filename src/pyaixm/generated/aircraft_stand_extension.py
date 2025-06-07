from dataclasses import dataclass

from generated.aircraft_stand_extension_type import AircraftStandExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AircraftStandExtension(AircraftStandExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
