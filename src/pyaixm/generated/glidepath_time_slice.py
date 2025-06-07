from dataclasses import dataclass

from pyaixm.generated.glidepath_time_slice_type import GlidepathTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GlidepathTimeSlice(GlidepathTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
