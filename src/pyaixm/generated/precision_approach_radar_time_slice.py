from dataclasses import dataclass

from generated.precision_approach_radar_time_slice_type import (
    PrecisionApproachRadarTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrecisionApproachRadarTimeSlice(PrecisionApproachRadarTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
