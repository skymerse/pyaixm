from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)
from generated.taxi_holding_position_light_system_time_slice_property_type import (
    TaxiHoldingPositionLightSystemTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystemType(AbstractGroundLightSystemType):
    time_slice: Iterable[
        TaxiHoldingPositionLightSystemTimeSlicePropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
