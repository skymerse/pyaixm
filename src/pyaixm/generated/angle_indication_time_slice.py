from dataclasses import dataclass

from generated.angle_indication_time_slice_type import (
    AngleIndicationTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleIndicationTimeSlice(AngleIndicationTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
