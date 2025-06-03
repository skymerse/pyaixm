from dataclasses import dataclass

from generated.operation_method_property_type import (
    OperationMethodPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationMethodRef(OperationMethodPropertyType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml/3.2"
