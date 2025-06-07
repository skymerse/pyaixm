from dataclasses import dataclass

from pyaixm.generated.primary_surveillance_radar_time_slice_type import (
    PrimarySurveillanceRadarTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadarTimeSlice(PrimarySurveillanceRadarTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
