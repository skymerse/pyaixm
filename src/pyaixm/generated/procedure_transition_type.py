from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_designated_point_designator_type import (
    CodeDesignatedPointDesignatorType,
)
from pyaixm.generated.code_procedure_phase_type import CodeProcedurePhaseType
from pyaixm.generated.curve_property_type_2 import CurvePropertyType2
from pyaixm.generated.landing_takeoff_area_collection_property_type import (
    LandingTakeoffAreaCollectionPropertyType,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.procedure_transition_leg_property_type import (
    ProcedureTransitionLegPropertyType,
)
from pyaixm.generated.procedure_transition_type_extension import (
    ProcedureTransitionTypeExtension,
)
from pyaixm.generated.text_instruction_type import TextInstructionType
from pyaixm.generated.val_bearing_type import ValBearingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransitionType(AbstractAixmobjectType):
    transition_id: Optional[CodeDesignatedPointDesignatorType] = field(
        default=None,
        metadata={
            "name": "transitionId",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeProcedurePhaseType] = field(
        default=None,
        metadata={
            "name": "type",
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
    vector_heading: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "vectorHeading",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    departure_runway_transition: Optional[
        LandingTakeoffAreaCollectionPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "departureRunwayTransition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    trajectory: Optional[CurvePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    transition_leg: Iterable[ProcedureTransitionLegPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transitionLeg",
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
    extension: Iterable[ProcedureTransitionTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
