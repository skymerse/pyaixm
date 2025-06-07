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
from generated.date_time_property_type import DateTimePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdUsageType(AbstractObjectType):
    """
    Brief description of ways in which the dataset is currently used.
    """

    class Meta:
        name = "MD_Usage_Type"

    specific_usage: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    usage_date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "usageDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_determined_limitations: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userDeterminedLimitations",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    user_contact_info: Iterable[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "userContactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
