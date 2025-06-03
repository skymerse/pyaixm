from dataclasses import dataclass

from generated.surveillance_radar_extension_type import (
    SurveillanceRadarExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SurveillanceRadarExtension(SurveillanceRadarExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
