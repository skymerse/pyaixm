from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from generated.ndbtime_slice_property_type import NdbtimeSlicePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Ndbtype(AbstractNavaidEquipmentType):
    class Meta:
        name = "NDBType"

    time_slice: Iterable[NdbtimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
