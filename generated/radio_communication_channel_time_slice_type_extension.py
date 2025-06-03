from dataclasses import dataclass, field
from typing import Optional

from generated.radio_communication_channel_extension import (
    RadioCommunicationChannelExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationChannelTimeSliceTypeExtension:
    class Meta:
        global_type = False

    radio_communication_channel_extension: Optional[
        RadioCommunicationChannelExtension
    ] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationChannelExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
