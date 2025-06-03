from dataclasses import dataclass

from generated.vortime_slice_type import VortimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VortimeSlice(VortimeSliceType):
    class Meta:
        name = "VORTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
