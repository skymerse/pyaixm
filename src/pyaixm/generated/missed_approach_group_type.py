from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.altimeter_source_property_type import (
    AltimeterSourcePropertyType,
)
from pyaixm.generated.missed_approach_group_type_extension import (
    MissedApproachGroupTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_instruction_type import TextInstructionType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachGroupType(AbstractAixmobjectType):
    instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    alternate_climb_instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "name": "alternateClimbInstruction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    alternate_climb_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "alternateClimbAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altimeter: Iterable[AltimeterSourcePropertyType] = field(
        default_factory=list,
        metadata={
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
    extension: Iterable[MissedApproachGroupTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
