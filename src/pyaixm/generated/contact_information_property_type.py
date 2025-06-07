from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.contact_information import ContactInformation

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ContactInformationPropertyType(AbstractAixmpropertyType):
    contact_information: Optional[ContactInformation] = field(
        default=None,
        metadata={
            "name": "ContactInformation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
