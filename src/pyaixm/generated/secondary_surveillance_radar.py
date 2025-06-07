from dataclasses import dataclass

from pyaixm.generated.secondary_surveillance_radar_type import (
    SecondarySurveillanceRadarType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SecondarySurveillanceRadar(SecondarySurveillanceRadarType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
