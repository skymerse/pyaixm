from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.aerial_refuelling_extension import (
    AerialRefuellingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    aerial_refuelling_extension: Optional[AerialRefuellingExtension] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingExtension",
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
