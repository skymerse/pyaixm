from dataclasses import dataclass

from pyaixm.generated.radar_component_type import RadarComponentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarComponent(RadarComponentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
