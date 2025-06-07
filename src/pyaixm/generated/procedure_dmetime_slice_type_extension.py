from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.procedure_dmeextension import ProcedureDmeextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ProcedureDmetimeSliceTypeExtension:
    class Meta:
        global_type = False

    procedure_dmeextension: Optional[ProcedureDmeextension] = field(
        default=None,
        metadata={
            "name": "ProcedureDMEExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
