from dataclasses import dataclass

from pyaixm.generated.aeronautical_ground_light_type import (
    AeronauticalGroundLightType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AeronauticalGroundLight(AeronauticalGroundLightType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
