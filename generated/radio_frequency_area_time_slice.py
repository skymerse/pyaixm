from dataclasses import dataclass

from generated.radio_frequency_area_time_slice_type import (
    RadioFrequencyAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioFrequencyAreaTimeSlice(RadioFrequencyAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
