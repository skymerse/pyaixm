from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from pyaixm.generated.md_identifier_type import CiCitationPropertyType
from pyaixm.generated.md_keyword_type_code_property_type import (
    MdKeywordTypeCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywordsType(AbstractObjectType):
    """
    Keywords, their type and reference source.
    """

    class Meta:
        name = "MD_Keywords_Type"

    keyword: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    type_value: Optional[MdKeywordTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    thesaurus_name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "thesaurusName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
