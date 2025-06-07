from dataclasses import dataclass

from pyaixm.generated.coordinate_system_property_type import (
    CoordinateSystemPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateSystemRef(CoordinateSystemPropertyType):
    class Meta:
        name = "coordinateSystemRef"
        namespace = "http://www.opengis.net/gml/3.2"
