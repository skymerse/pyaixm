from dataclasses import dataclass

from generated.coordinate_operation_property_type import (
    CoordinateOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateOperationRef(CoordinateOperationPropertyType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"
