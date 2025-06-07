from dataclasses import dataclass

from pyaixm.generated.pilot_controlled_lighting_time_slice_type import (
    PilotControlledLightingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLightingTimeSlice(PilotControlledLightingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
