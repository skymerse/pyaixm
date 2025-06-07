from dataclasses import dataclass

from pyaixm.generated.sdftime_slice_type import SdftimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SdftimeSlice(SdftimeSliceType):
    class Meta:
        name = "SDFTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
