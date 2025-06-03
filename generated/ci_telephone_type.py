from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_object_type import AbstractObjectType
from generated.character_string_property_type import (
    CharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiTelephoneType(AbstractObjectType):
    """
    Telephone numbers for contacting the responsible individual or organisation.
    """

    class Meta:
        name = "CI_Telephone_Type"

    voice: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    facsimile: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
