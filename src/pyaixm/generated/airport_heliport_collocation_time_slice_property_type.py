from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_heliport_collocation_time_slice import (
    AirportHeliportCollocationTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportCollocationTimeSlicePropertyType:
    airport_heliport_collocation_time_slice: Optional[
        AirportHeliportCollocationTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportCollocationTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
