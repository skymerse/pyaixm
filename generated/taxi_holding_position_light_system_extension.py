from dataclasses import dataclass

from generated.taxi_holding_position_light_system_extension_type import (
    TaxiHoldingPositionLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiHoldingPositionLightSystemExtension(
    TaxiHoldingPositionLightSystemExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
