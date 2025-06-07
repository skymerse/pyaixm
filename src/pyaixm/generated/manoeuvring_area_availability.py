from dataclasses import dataclass

from generated.manoeuvring_area_availability_type import (
    ManoeuvringAreaAvailabilityType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaAvailability(ManoeuvringAreaAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
