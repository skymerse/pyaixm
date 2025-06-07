from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.aircraft_characteristic import AircraftCharacteristic

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftCharacteristicPropertyType(AbstractAixmpropertyType):
    aircraft_characteristic: Optional[AircraftCharacteristic] = field(
        default=None,
        metadata={
            "name": "AircraftCharacteristic",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
