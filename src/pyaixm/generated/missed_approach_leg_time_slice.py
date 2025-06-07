from dataclasses import dataclass

from generated.missed_approach_leg_time_slice_type import (
    MissedApproachLegTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachLegTimeSlice(MissedApproachLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
