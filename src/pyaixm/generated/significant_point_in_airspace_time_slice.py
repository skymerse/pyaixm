from dataclasses import dataclass

from generated.significant_point_in_airspace_time_slice_type import (
    SignificantPointInAirspaceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SignificantPointInAirspaceTimeSlice(
    SignificantPointInAirspaceTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
