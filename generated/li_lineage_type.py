from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_object_type import AbstractObjectType
from generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from generated.li_process_step_type import (
    LiProcessStepPropertyType,
    LiSourcePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiLineageType(AbstractObjectType):
    class Meta:
        name = "LI_Lineage_Type"

    statement: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    process_step: Iterable[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "processStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    source: Iterable[LiSourcePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
