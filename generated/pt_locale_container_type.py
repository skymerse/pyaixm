from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.ci_date_property_type import CiDatePropertyType
from generated.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from generated.localised_character_string_property_type import (
    LocalisedCharacterStringPropertyType,
)
from generated.pt_locale_property_type import PtLocalePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleContainerType:
    class Meta:
        name = "PT_LocaleContainer_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    locale: Optional[PtLocalePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    date: Iterable[CiDatePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    responsible_party: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    localised_string: Iterable[LocalisedCharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "localisedString",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
