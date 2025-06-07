from dataclasses import dataclass

from generated.unit_time_slice_type import UnitTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitTimeSlice(UnitTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
