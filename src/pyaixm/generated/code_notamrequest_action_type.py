from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_notamrequest_action_base_type import (
    CodeNotamrequestActionBaseType,
)
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class CodeNotamrequestActionType:
    class Meta:
        name = "CodeNOTAMRequestActionType"

    value: Optional[CodeNotamrequestActionBaseType] = field(
        default=None,
        metadata={
            "required": True,
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
