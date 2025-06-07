from dataclasses import dataclass

from pyaixm.generated.airspace_volume_type import AirspaceVolumeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceVolume(AirspaceVolumeType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
