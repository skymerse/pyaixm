from dataclasses import dataclass

from generated.tacantime_slice_type import TacantimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TacantimeSlice(TacantimeSliceType):
    class Meta:
        name = "TACANTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
