from dataclasses import dataclass

from pyaixm.generated.airport_protection_area_marking_time_slice_type import (
    AirportProtectionAreaMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportProtectionAreaMarkingTimeSlice(
    AirportProtectionAreaMarkingTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
