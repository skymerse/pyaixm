from dataclasses import dataclass, field
from typing import Optional

from generated.aircraft_characteristic_extension import (
    AircraftCharacteristicExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftCharacteristicTypeExtension:
    class Meta:
        global_type = False

    aircraft_characteristic_extension: Optional[
        AircraftCharacteristicExtension
    ] = field(
        default=None,
        metadata={
            "name": "AircraftCharacteristicExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
