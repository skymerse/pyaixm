from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.localised_character_string_property_type import (
    LocalisedCharacterStringPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtFreeTextType(AbstractObjectType):
    class Meta:
        name = "PT_FreeText_Type"

    text_group: Iterable[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "textGroup",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
