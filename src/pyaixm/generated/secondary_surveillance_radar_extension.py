from dataclasses import dataclass

from generated.secondary_surveillance_radar_extension_type import (
    SecondarySurveillanceRadarExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SecondarySurveillanceRadarExtension(
    SecondarySurveillanceRadarExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
