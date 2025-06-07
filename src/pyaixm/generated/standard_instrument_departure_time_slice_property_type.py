from dataclasses import dataclass, field
from typing import Optional

from generated.standard_instrument_departure_time_slice import (
    StandardInstrumentDepartureTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardInstrumentDepartureTimeSlicePropertyType:
    standard_instrument_departure_time_slice: Optional[
        StandardInstrumentDepartureTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "StandardInstrumentDepartureTimeSlice",
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
