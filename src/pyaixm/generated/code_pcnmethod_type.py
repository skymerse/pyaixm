from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_pcnmethod_base_type_value import CodePcnmethodBaseTypeValue
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodePcnmethodType:
    class Meta:
        name = "CodePCNMethodType"

    value: Union[str, CodePcnmethodBaseTypeValue] = field(
        default="",
        metadata={
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
