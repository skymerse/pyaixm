from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.time_calendar_era_property_type import (
    TimeCalendarEraPropertyType,
)
from generated.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCalendarType(TimeReferenceSystemType):
    reference_frame: Iterable[TimeCalendarEraPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "referenceFrame",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
