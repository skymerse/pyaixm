from dataclasses import dataclass, field
from typing import Optional

from generated.procedure_dmetime_slice import ProcedureDmetimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureDmetimeSlicePropertyType:
    class Meta:
        name = "ProcedureDMETimeSlicePropertyType"

    procedure_dmetime_slice: Optional[ProcedureDmetimeSlice] = field(
        default=None,
        metadata={
            "name": "ProcedureDMETimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
