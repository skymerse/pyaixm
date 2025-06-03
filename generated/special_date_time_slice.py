from dataclasses import dataclass

from generated.special_date_time_slice_type import SpecialDateTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialDateTimeSlice(SpecialDateTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
