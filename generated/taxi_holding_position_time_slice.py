from dataclasses import dataclass

from generated.taxi_holding_position_time_slice_type import (
    TaxiHoldingPositionTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionTimeSlice(TaxiHoldingPositionTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
