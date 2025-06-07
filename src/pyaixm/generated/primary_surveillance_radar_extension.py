from dataclasses import dataclass

from generated.primary_surveillance_radar_extension_type import (
    PrimarySurveillanceRadarExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class PrimarySurveillanceRadarExtension(PrimarySurveillanceRadarExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
