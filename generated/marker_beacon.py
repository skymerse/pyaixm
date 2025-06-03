from dataclasses import dataclass

from generated.marker_beacon_type import MarkerBeaconType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkerBeacon(MarkerBeaconType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
