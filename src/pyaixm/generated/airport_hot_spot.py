from dataclasses import dataclass

from pyaixm.generated.airport_hot_spot_type import AirportHotSpotType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHotSpot(AirportHotSpotType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
