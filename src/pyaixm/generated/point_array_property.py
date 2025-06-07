from dataclasses import dataclass

from pyaixm.generated.point_array_property_type import PointArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayProperty(PointArrayPropertyType):
    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"
