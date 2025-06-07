from dataclasses import dataclass

from generated.significant_point_in_airspace_extension_type import (
    SignificantPointInAirspaceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SignificantPointInAirspaceExtension(
    SignificantPointInAirspaceExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
