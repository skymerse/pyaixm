from dataclasses import dataclass

from generated.unit_availability_type import UnitAvailabilityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitAvailability(UnitAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
