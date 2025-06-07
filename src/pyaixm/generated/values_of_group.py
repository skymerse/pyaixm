from dataclasses import dataclass

from generated.operation_parameter_group_property_type import (
    OperationParameterGroupPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValuesOfGroup(OperationParameterGroupPropertyType):
    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml/3.2"
