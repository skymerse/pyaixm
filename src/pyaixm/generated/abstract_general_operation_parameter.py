from dataclasses import dataclass

from pyaixm.generated.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralOperationParameter(AbstractGeneralOperationParameterType):
    """
    Gml:GeneralOperationParameter is the abstract definition of a parameter or
    group of parameters used by an operation method.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
