from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.no_sequence_type import NoSequenceType
from generated.note_property_type import NotePropertyType
from generated.procedure_transition_leg_type_extension import (
    ProcedureTransitionLegTypeExtension,
)
from generated.segment_leg_property_type import SegmentLegPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransitionLegType(AbstractAixmobjectType):
    seq_number_arinc: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "seqNumberARINC",
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
    the_segment_leg: Optional[SegmentLegPropertyType] = field(
        default=None,
        metadata={
            "name": "theSegmentLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[ProcedureTransitionLegTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
