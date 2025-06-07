from dataclasses import dataclass

from generated.fire_fighting_service_time_slice_type import (
    FireFightingServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FireFightingServiceTimeSlice(FireFightingServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
