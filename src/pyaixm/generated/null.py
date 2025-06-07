from dataclasses import dataclass, field
from typing import Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    value: Union[str, NilReasonEnumerationValue] = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"other:\w{2,}",
        },
    )
