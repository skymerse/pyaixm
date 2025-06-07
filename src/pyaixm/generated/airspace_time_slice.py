from dataclasses import dataclass

from pyaixm.generated.airspace_time_slice_type import AirspaceTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceTimeSlice(AirspaceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
