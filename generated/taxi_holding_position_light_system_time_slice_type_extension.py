from dataclasses import dataclass, field
from typing import Optional

from generated.ground_light_system_extension import GroundLightSystemExtension
from generated.taxi_holding_position_light_system_extension import (
    TaxiHoldingPositionLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxi_holding_position_light_system_extension: Optional[
        TaxiHoldingPositionLightSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionLightSystemExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    ground_light_system_extension: Optional[GroundLightSystemExtension] = (
        field(
            default=None,
            metadata={
                "name": "GroundLightSystemExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
