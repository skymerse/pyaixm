from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.airport_sign_time_slice_property_type import (
    AirportSignTimeSlicePropertyType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportSignType(AbstractAixmfeatureType):
    time_slice: Iterable[AirportSignTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "min_occurs": 1,
        },
    )
