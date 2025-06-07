from dataclasses import dataclass

from generated.safe_altitude_area_type import SafeAltitudeAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeArea(SafeAltitudeAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
