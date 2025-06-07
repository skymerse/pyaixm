from dataclasses import dataclass

from pyaixm.generated.point_property_type_1 import PointPropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointRep(PointPropertyType1):
    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml/3.2"
