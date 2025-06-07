from dataclasses import dataclass

from pyaixm.generated.precision_approach_radar_type import (
    PrecisionApproachRadarType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrecisionApproachRadar(PrecisionApproachRadarType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
