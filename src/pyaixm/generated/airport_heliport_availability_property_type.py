from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.airport_heliport_availability import AirportHeliportAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportAvailabilityPropertyType(AbstractAixmpropertyType):
    airport_heliport_availability: Optional[AirportHeliportAvailability] = (
        field(
            default=None,
            metadata={
                "name": "AirportHeliportAvailability",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
