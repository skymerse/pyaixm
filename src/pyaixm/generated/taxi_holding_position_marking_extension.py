from dataclasses import dataclass

from generated.taxi_holding_position_marking_extension_type import (
    TaxiHoldingPositionMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiHoldingPositionMarkingExtension(
    TaxiHoldingPositionMarkingExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
