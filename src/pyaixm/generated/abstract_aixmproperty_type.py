from dataclasses import dataclass, field
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmpropertyType:
    """It provides a basis for deriving AIXM feature/object properties.

    It defines the nilReason attribute and currently, it is only used
    for properties that are derived from association with an AIM object.
    """

    class Meta:
        name = "AbstractAIXMPropertyType"

    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
