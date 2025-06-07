from dataclasses import dataclass

from generated.search_rescue_service_time_slice_type import (
    SearchRescueServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SearchRescueServiceTimeSlice(SearchRescueServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
