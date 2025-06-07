from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.character_string_property_type import (
    CharacterStringPropertyType,
)
from pyaixm.generated.integer_property_type import IntegerPropertyType
from pyaixm.generated.md_medium_format_code_property_type import (
    MdMediumFormatCodePropertyType,
)
from pyaixm.generated.md_medium_name_code_property_type import (
    MdMediumNameCodePropertyType,
)
from pyaixm.generated.real_property_type import RealPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumType(AbstractObjectType):
    """
    Information about the media on which the data can be distributed.
    """

    class Meta:
        name = "MD_Medium_Type"

    name: Optional[MdMediumNameCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    density: Iterable[RealPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    density_units: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "densityUnits",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    volumes: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    medium_format: Iterable[MdMediumFormatCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "mediumFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    medium_note: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "mediumNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
