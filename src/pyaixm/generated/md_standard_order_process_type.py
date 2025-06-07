from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_object_type import AbstractObjectType
from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.date_time_property_type import DateTimePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdStandardOrderProcessType(AbstractObjectType):
    """
    Common ways in which the dataset may be obtained or received, and related
    instructions and fee information.
    """

    class Meta:
        name = "MD_StandardOrderProcess_Type"

    fees: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    planned_available_date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "plannedAvailableDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ordering_instructions: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "orderingInstructions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    turnaround: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
