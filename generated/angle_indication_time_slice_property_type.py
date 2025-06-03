from dataclasses import dataclass, field
from typing import Optional

from generated.angle_indication_time_slice import AngleIndicationTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleIndicationTimeSlicePropertyType:
    angle_indication_time_slice: Optional[AngleIndicationTimeSlice] = field(
        default=None,
        metadata={
            "name": "AngleIndicationTimeSlice",
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
