from dataclasses import dataclass

from pyaixm.generated.taxi_holding_position_light_system_type import (
    TaxiHoldingPositionLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystem(TaxiHoldingPositionLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
