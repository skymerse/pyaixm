from dataclasses import dataclass

from generated.radar_system_time_slice_type import RadarSystemTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarSystemTimeSlice(RadarSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
