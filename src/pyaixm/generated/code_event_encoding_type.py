from dataclasses import dataclass, field
from typing import Union

from generated.code_event_encoding_base_type_value import (
    CodeEventEncodingBaseTypeValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class CodeEventEncodingType:
    value: Union[str, CodeEventEncodingBaseTypeValue] = field(
        default="",
        metadata={
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
