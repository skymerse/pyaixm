from dataclasses import dataclass

from generated.azimuth_time_slice_type import AzimuthTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AzimuthTimeSlice(AzimuthTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
