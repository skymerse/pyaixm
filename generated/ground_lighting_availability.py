from dataclasses import dataclass

from generated.ground_lighting_availability_type import (
    GroundLightingAvailabilityType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundLightingAvailability(GroundLightingAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
