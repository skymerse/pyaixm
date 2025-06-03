from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.flight_restriction_level_type_extension import (
    FlightRestrictionLevelTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionLevelType(AbstractAixmobjectType):
    upper_level: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_level_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "upperLevelReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_level: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_level_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "lowerLevelReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[FlightRestrictionLevelTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
