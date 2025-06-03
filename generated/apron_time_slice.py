from dataclasses import dataclass

from generated.apron_time_slice_type import ApronTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronTimeSlice(ApronTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
