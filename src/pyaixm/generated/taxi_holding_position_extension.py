from dataclasses import dataclass

from generated.taxi_holding_position_extension_type import (
    TaxiHoldingPositionExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiHoldingPositionExtension(TaxiHoldingPositionExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
