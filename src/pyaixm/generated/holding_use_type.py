from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_holding_use_type import CodeHoldingUseType
from pyaixm.generated.code_vertical_reference_type import (
    CodeVerticalReferenceType,
)
from pyaixm.generated.holding_pattern_property_type import (
    HoldingPatternPropertyType,
)
from pyaixm.generated.holding_use_type_extension import HoldingUseTypeExtension
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.text_instruction_type import TextInstructionType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingUseType(AbstractAixmobjectType):
    holding_use: Optional[CodeHoldingUseType] = field(
        default=None,
        metadata={
            "name": "holdingUse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    instructed_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "instructedAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    instruction_altitude_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "instructionAltitudeReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    the_holding_pattern: Optional[HoldingPatternPropertyType] = field(
        default=None,
        metadata={
            "name": "theHoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[HoldingUseTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
