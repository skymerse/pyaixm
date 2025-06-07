from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.telephone_contact import TelephoneContact

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TelephoneContactPropertyType(AbstractAixmpropertyType):
    telephone_contact: Optional[TelephoneContact] = field(
        default=None,
        metadata={
            "name": "TelephoneContact",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
