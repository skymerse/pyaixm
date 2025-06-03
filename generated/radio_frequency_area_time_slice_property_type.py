from dataclasses import dataclass, field
from typing import Optional

from generated.radio_frequency_area_time_slice import (
    RadioFrequencyAreaTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioFrequencyAreaTimeSlicePropertyType:
    radio_frequency_area_time_slice: Optional[RadioFrequencyAreaTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "RadioFrequencyAreaTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
