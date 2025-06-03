from dataclasses import dataclass

from generated.secondary_surveillance_radar_time_slice_type import (
    SecondarySurveillanceRadarTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SecondarySurveillanceRadarTimeSlice(
    SecondarySurveillanceRadarTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
