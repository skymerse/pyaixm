from dataclasses import dataclass

from generated.airspace_border_crossing_type import AirspaceBorderCrossingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceBorderCrossing(AirspaceBorderCrossingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
