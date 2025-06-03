from dataclasses import dataclass

from generated.point_property_type_1 import PointPropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CenterOf(PointPropertyType1):
    class Meta:
        name = "centerOf"
        namespace = "http://www.opengis.net/gml/3.2"
