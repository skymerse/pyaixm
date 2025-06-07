from dataclasses import dataclass

from pyaixm.generated.radio_communication_channel_extension_type import (
    RadioCommunicationChannelExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RadioCommunicationChannelExtension(
    RadioCommunicationChannelExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
