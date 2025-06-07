from dataclasses import dataclass, field
from typing import Optional

from generated.aircraft_stand_extension import AircraftStandExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandTimeSliceTypeExtension:
    class Meta:
        global_type = False

    aircraft_stand_extension: Optional[AircraftStandExtension] = field(
        default=None,
        metadata={
            "name": "AircraftStandExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
