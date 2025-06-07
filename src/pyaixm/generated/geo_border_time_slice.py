from dataclasses import dataclass

from pyaixm.generated.geo_border_time_slice_type import GeoBorderTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GeoBorderTimeSlice(GeoBorderTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
