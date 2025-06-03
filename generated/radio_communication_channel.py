from dataclasses import dataclass

from generated.radio_communication_channel_type import (
    RadioCommunicationChannelType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationChannel(RadioCommunicationChannelType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
