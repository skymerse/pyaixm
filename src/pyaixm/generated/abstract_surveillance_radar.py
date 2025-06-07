from dataclasses import dataclass

from pyaixm.generated.abstract_surveillance_radar_type import (
    AbstractSurveillanceRadarType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSurveillanceRadar(AbstractSurveillanceRadarType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
