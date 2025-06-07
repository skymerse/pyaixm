from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.online_contact import OnlineContact

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OnlineContactPropertyType(AbstractAixmpropertyType):
    online_contact: Optional[OnlineContact] = field(
        default=None,
        metadata={
            "name": "OnlineContact",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
