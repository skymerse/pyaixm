from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.standard_level_sector_time_slice_property_type import (
    StandardLevelSectorTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSectorType(AbstractAixmfeatureType):
    time_slice: Iterable[StandardLevelSectorTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
