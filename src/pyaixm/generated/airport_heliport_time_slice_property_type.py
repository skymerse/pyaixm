from dataclasses import dataclass, field
from typing import Optional

from generated.airport_heliport_time_slice import AirportHeliportTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportTimeSlicePropertyType:
    airport_heliport_time_slice: Optional[AirportHeliportTimeSlice] = field(
        default=None,
        metadata={
            "name": "AirportHeliportTimeSlice",
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
