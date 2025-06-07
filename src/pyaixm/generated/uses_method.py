from dataclasses import dataclass

from pyaixm.generated.operation_method_property_type import (
    OperationMethodPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesMethod(OperationMethodPropertyType):
    class Meta:
        name = "usesMethod"
        namespace = "http://www.opengis.net/gml/3.2"
