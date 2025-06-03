from dataclasses import dataclass

from generated.surface_array_property_type import SurfaceArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceArrayProperty(SurfaceArrayPropertyType):
    class Meta:
        name = "surfaceArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"
