from dataclasses import dataclass

from pyaixm.generated.surveillance_ground_station_type import (
    SurveillanceGroundStationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveillanceGroundStation(SurveillanceGroundStationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
