from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.rules_procedures_time_slice import (
    RulesProceduresTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RulesProceduresTimeSlicePropertyType:
    rules_procedures_time_slice: Optional[RulesProceduresTimeSlice] = field(
        default=None,
        metadata={
            "name": "RulesProceduresTimeSlice",
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
