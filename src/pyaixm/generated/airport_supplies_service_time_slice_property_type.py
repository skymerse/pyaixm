from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_supplies_service_time_slice import (
    AirportSuppliesServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesServiceTimeSlicePropertyType:
    airport_supplies_service_time_slice: Optional[
        AirportSuppliesServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirportSuppliesServiceTimeSlice",
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
