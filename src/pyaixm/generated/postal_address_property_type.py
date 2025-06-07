from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.postal_address import PostalAddress

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PostalAddressPropertyType(AbstractAixmpropertyType):
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
