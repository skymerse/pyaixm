from dataclasses import dataclass

from pyaixm.generated.radio_communication_channel_time_slice_type import (
    RadioCommunicationChannelTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationChannelTimeSlice(
    RadioCommunicationChannelTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
