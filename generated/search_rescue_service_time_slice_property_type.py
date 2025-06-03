from dataclasses import dataclass, field
from typing import Optional

from generated.search_rescue_service_time_slice import (
    SearchRescueServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SearchRescueServiceTimeSlicePropertyType:
    search_rescue_service_time_slice: Optional[
        SearchRescueServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SearchRescueServiceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
