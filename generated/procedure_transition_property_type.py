from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.procedure_transition import ProcedureTransition

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureTransitionPropertyType(AbstractAixmpropertyType):
    procedure_transition: Optional[ProcedureTransition] = field(
        default=None,
        metadata={
            "name": "ProcedureTransition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
