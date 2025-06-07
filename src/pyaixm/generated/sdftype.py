from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)
from pyaixm.generated.sdftime_slice_property_type import (
    SdftimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Sdftype(AbstractNavaidEquipmentType):
    class Meta:
        name = "SDFType"

    time_slice: Iterable[SdftimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
