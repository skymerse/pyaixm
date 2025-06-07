from dataclasses import dataclass

from generated.multi_surface_property_type import MultiSurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiExtentOf(MultiSurfacePropertyType):
    class Meta:
        name = "multiExtentOf"
        namespace = "http://www.opengis.net/gml/3.2"
