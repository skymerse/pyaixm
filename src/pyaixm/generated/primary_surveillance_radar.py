from dataclasses import dataclass

from pyaixm.generated.primary_surveillance_radar_type import (
    PrimarySurveillanceRadarType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadar(PrimarySurveillanceRadarType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
