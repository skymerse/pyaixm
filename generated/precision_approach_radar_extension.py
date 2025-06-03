from dataclasses import dataclass

from generated.precision_approach_radar_extension_type import (
    PrecisionApproachRadarExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class PrecisionApproachRadarExtension(PrecisionApproachRadarExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
