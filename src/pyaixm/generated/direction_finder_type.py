from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from pyaixm.generated.direction_finder_time_slice_property_type import (
    DirectionFinderTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectionFinderType(AbstractNavaidEquipmentType):
    time_slice: Iterable[DirectionFinderTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
