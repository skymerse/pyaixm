from dataclasses import dataclass

from pyaixm.generated.marker_beacon_extension_type import (
    MarkerBeaconExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class MarkerBeaconExtension(MarkerBeaconExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
