from dataclasses import dataclass

from pyaixm.generated.approach_lighting_system_time_slice_type import (
    ApproachLightingSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystemTimeSlice(ApproachLightingSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
