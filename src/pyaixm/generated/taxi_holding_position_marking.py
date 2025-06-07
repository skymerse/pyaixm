from dataclasses import dataclass

from pyaixm.generated.taxi_holding_position_marking_type import (
    TaxiHoldingPositionMarkingType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionMarking(TaxiHoldingPositionMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
