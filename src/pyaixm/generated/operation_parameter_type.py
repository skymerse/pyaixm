from dataclasses import dataclass

from pyaixm.generated.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameterType(AbstractGeneralOperationParameterType):
    pass
