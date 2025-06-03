from dataclasses import dataclass

from generated.taxi_holding_position_type import TaxiHoldingPositionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPosition(TaxiHoldingPositionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
