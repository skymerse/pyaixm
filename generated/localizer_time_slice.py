from dataclasses import dataclass

from generated.localizer_time_slice_type import LocalizerTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LocalizerTimeSlice(LocalizerTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
