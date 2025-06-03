from dataclasses import dataclass

from generated.surface_property_type_1 import SurfacePropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ExtentOf(SurfacePropertyType1):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml/3.2"
