from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.procedure_availability import ProcedureAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureAvailabilityPropertyType(AbstractAixmpropertyType):
    procedure_availability: Optional[ProcedureAvailability] = field(
        default=None,
        metadata={
            "name": "ProcedureAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
