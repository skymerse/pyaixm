from dataclasses import dataclass, field
from typing import Optional

from generated.radio_communication_channel_time_slice import (
    RadioCommunicationChannelTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationChannelTimeSlicePropertyType:
    radio_communication_channel_time_slice: Optional[
        RadioCommunicationChannelTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationChannelTimeSlice",
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
