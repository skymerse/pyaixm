from dataclasses import dataclass, field
from typing import Optional

from generated.standard_instrument_arrival_time_slice import (
    StandardInstrumentArrivalTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentArrivalTimeSlicePropertyType:
    standard_instrument_arrival_time_slice: Optional[
        StandardInstrumentArrivalTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentArrivalTimeSlice",
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
