from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.procedure_transition_leg import ProcedureTransitionLeg

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransitionLegPropertyType(AbstractAixmpropertyType):
    procedure_transition_leg: Optional[ProcedureTransitionLeg] = field(
        default=None,
        metadata={
            "name": "ProcedureTransitionLeg",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
