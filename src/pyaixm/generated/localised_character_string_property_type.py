from dataclasses import dataclass, field
from typing import Optional

from generated.localised_character_string import LocalisedCharacterString
from generated.object_reference_property_type import (
    ObjectReferencePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LocalisedCharacterStringPropertyType(ObjectReferencePropertyType):
    class Meta:
        name = "LocalisedCharacterString_PropertyType"

    localised_character_string: Optional[LocalisedCharacterString] = field(
        default=None,
        metadata={
            "name": "LocalisedCharacterString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
