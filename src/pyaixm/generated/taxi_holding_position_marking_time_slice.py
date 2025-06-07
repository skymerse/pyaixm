from dataclasses import dataclass

from pyaixm.generated.taxi_holding_position_marking_time_slice_type import (
    TaxiHoldingPositionMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionMarkingTimeSlice(
    TaxiHoldingPositionMarkingTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
