from dataclasses import dataclass

from pyaixm.generated.holding_pattern_time_slice_type import (
    HoldingPatternTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternTimeSlice(HoldingPatternTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
