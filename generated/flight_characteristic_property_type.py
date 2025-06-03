from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.flight_characteristic import FlightCharacteristic

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightCharacteristicPropertyType(AbstractAixmpropertyType):
    flight_characteristic: Optional[FlightCharacteristic] = field(
        default=None,
        metadata={
            "name": "FlightCharacteristic",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
