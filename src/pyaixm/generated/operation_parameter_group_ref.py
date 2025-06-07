from dataclasses import dataclass

from generated.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameterGroupRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterGroupRef"
        namespace = "http://www.opengis.net/gml/3.2"
