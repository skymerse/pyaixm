from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CountList:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"

    value: Iterable[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
