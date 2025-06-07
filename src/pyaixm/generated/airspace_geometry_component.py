from dataclasses import dataclass

from generated.airspace_geometry_component_type import (
    AirspaceGeometryComponentType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceGeometryComponent(AirspaceGeometryComponentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
