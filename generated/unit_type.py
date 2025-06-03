from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.unit_time_slice_property_type import UnitTimeSlicePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitType(AbstractAixmfeatureType):
    time_slice: Iterable[UnitTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
