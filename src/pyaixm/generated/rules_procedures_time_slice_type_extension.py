from dataclasses import dataclass, field
from typing import Optional

from generated.rules_procedures_extension import RulesProceduresExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RulesProceduresTimeSliceTypeExtension:
    class Meta:
        global_type = False

    rules_procedures_extension: Optional[RulesProceduresExtension] = field(
        default=None,
        metadata={
            "name": "RulesProceduresExtension",
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
