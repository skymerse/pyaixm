from dataclasses import dataclass

from pyaixm.generated.altimeter_source_time_slice_type import (
    AltimeterSourceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSourceTimeSlice(AltimeterSourceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
