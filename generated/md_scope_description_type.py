from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.object_reference_property_type import (
    ObjectReferencePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionType:
    """
    Description of the class of information covered by the information.
    """

    class Meta:
        name = "MD_ScopeDescription_Type"

    attributes: Iterable[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    features: Iterable[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    feature_instances: Iterable[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    attribute_instances: Iterable[ObjectReferencePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "attributeInstances",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dataset: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    other: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
