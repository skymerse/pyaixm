from dataclasses import dataclass

from generated.ndbtime_slice_type import NdbtimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NdbtimeSlice(NdbtimeSliceType):
    class Meta:
        name = "NDBTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
