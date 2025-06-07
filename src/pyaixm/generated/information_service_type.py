from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_service_type import AbstractServiceType
from pyaixm.generated.information_service_time_slice_property_type import (
    InformationServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationServiceType(AbstractServiceType):
    time_slice: Iterable[InformationServiceTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
