from dataclasses import dataclass

from generated.airspace_volume_dependency_type import (
    AirspaceVolumeDependencyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceVolumeDependency(AirspaceVolumeDependencyType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
