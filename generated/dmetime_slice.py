from dataclasses import dataclass

from generated.dmetime_slice_type import DmetimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DmetimeSlice(DmetimeSliceType):
    class Meta:
        name = "DMETimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
