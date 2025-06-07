from dataclasses import dataclass

from pyaixm.generated.unplanned_holding_time_slice_type import (
    UnplannedHoldingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnplannedHoldingTimeSlice(UnplannedHoldingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
