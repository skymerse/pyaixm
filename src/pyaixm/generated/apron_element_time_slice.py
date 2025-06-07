from dataclasses import dataclass

from pyaixm.generated.apron_element_time_slice_type import (
    ApronElementTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronElementTimeSlice(ApronElementTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
