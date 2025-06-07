from dataclasses import dataclass, field
from typing import Optional

from generated.airport_heliport_collocation_extension import (
    AirportHeliportCollocationExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportCollocationTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airport_heliport_collocation_extension: Optional[
        AirportHeliportCollocationExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportCollocationExtension",
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
