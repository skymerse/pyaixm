from dataclasses import dataclass

from generated.apron_area_availability_type import ApronAreaAvailabilityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronAreaAvailability(ApronAreaAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
