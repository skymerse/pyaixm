from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from generated.localizer_time_slice_property_type import (
    LocalizerTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LocalizerType(AbstractNavaidEquipmentType):
    time_slice: Iterable[LocalizerTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
