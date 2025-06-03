from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.direct_flight_class import DirectFlightClass

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectFlightClassPropertyType(AbstractAixmpropertyType):
    direct_flight_class: Optional[DirectFlightClass] = field(
        default=None,
        metadata={
            "name": "DirectFlightClass",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
