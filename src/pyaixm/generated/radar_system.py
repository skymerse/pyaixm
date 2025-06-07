from dataclasses import dataclass

from pyaixm.generated.radar_system_type import RadarSystemType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarSystem(RadarSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
