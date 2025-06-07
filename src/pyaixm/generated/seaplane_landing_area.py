from dataclasses import dataclass

from pyaixm.generated.seaplane_landing_area_type import SeaplaneLandingAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneLandingArea(SeaplaneLandingAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
