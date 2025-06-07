from dataclasses import dataclass, field
from typing import Optional

from generated.arrival_feeder_leg_time_slice import ArrivalFeederLegTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalFeederLegTimeSlicePropertyType:
    arrival_feeder_leg_time_slice: Optional[ArrivalFeederLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "ArrivalFeederLegTimeSlice",
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
