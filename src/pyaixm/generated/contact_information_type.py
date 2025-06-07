from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.contact_information_type_extension import (
    ContactInformationTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.online_contact_property_type import (
    OnlineContactPropertyType,
)
from pyaixm.generated.postal_address_property_type import (
    PostalAddressPropertyType,
)
from pyaixm.generated.telephone_contact_property_type import (
    TelephoneContactPropertyType,
)
from pyaixm.generated.text_name_type import TextNameType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ContactInformationType(AbstractAixmobjectType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    title: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    address: Iterable[PostalAddressPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    network_node: Iterable[OnlineContactPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "networkNode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    phone_fax: Iterable[TelephoneContactPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "phoneFax",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ContactInformationTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
