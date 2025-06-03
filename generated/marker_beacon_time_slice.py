from dataclasses import dataclass

from generated.marker_beacon_time_slice_type import MarkerBeaconTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkerBeaconTimeSlice(MarkerBeaconTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
