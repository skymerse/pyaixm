from dataclasses import dataclass, field
from typing import Optional

from generated.radio_frequency_area_extension import (
    RadioFrequencyAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioFrequencyAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    radio_frequency_area_extension: Optional[RadioFrequencyAreaExtension] = (
        field(
            default=None,
            metadata={
                "name": "RadioFrequencyAreaExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
