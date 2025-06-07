from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from generated.tacantime_slice_property_type import TacantimeSlicePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Tacantype(AbstractNavaidEquipmentType):
    class Meta:
        name = "TACANType"

    time_slice: Iterable[TacantimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
