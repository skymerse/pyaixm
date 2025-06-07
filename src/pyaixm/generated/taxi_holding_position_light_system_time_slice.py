from dataclasses import dataclass

from pyaixm.generated.taxi_holding_position_light_system_time_slice_type import (
    TaxiHoldingPositionLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystemTimeSlice(
    TaxiHoldingPositionLightSystemTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
