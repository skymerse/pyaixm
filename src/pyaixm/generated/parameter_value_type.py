from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from pyaixm.generated.boolean_value import BooleanValue
from pyaixm.generated.dms_angle_value import DmsAngleValue
from pyaixm.generated.integer_value import IntegerValue
from pyaixm.generated.integer_value_list import IntegerValueList
from pyaixm.generated.operation_parameter_2 import OperationParameter2
from pyaixm.generated.string_value import StringValue
from pyaixm.generated.value import Value
from pyaixm.generated.value_file import ValueFile
from pyaixm.generated.value_list import ValueList
from pyaixm.generated.value_of_parameter import ValueOfParameter

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dms_angle_value: Optional[DmsAngleValue] = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    string_value: Optional[StringValue] = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    integer_value: Optional[IntegerValue] = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    boolean_value: Optional[BooleanValue] = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_list: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    integer_value_list: Optional[IntegerValueList] = field(
        default=None,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_file: Optional[ValueFile] = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_of_parameter: Optional[ValueOfParameter] = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter: Optional[OperationParameter2] = field(
        default=None,
        metadata={
            "name": "operationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
