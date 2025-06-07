from dataclasses import dataclass

from pyaixm.generated.multi_geometry_property_type import (
    MultiGeometryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml/3.2"
