from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_extension_type import AbstractExtensionType
from pyaixm.generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from pyaixm.generated.code_cardinal_direction_type import (
    CodeCardinalDirectionType,
)
from pyaixm.generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class VerticalStructureExtensionType2(AbstractExtensionType):
    class Meta:
        name = "VerticalStructureExtensionType"

    distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    cardinal_direction: Optional[CodeCardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
    closest_airport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "closestAirport",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "nillable": True,
        },
    )
