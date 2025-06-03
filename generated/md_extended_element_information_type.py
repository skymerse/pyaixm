from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_object_type import AbstractObjectType
from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.ci_responsible_party_property_type import (
    CiResponsiblePartyPropertyType,
)
from generated.integer_property_type import IntegerPropertyType
from generated.md_datatype_code_property_type import MdDatatypeCodePropertyType
from generated.md_obligation_code_property_type import (
    MdObligationCodePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdExtendedElementInformationType(AbstractObjectType):
    """
    New metadata element, not found in ISO 19115, which is required to describe
    geographic data.
    """

    class Meta:
        name = "MD_ExtendedElementInformation_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    short_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "shortName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    domain_code: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "domainCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    definition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    obligation: Optional[MdObligationCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    condition: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    data_type: Optional[MdDatatypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dataType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    maximum_occurrence: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumOccurrence",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    domain_value: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "domainValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    parent_entity: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "parentEntity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
    rule: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    rationale: Iterable[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
