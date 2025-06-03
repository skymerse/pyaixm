from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from generated.dmetime_slice_property_type import DmetimeSlicePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Dmetype(AbstractNavaidEquipmentType):
    class Meta:
        name = "DMEType"

    time_slice: Iterable[DmetimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
