from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.distance_indication_extension import (
    DistanceIndicationExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DistanceIndicationTimeSliceTypeExtension:
    class Meta:
        global_type = False

    distance_indication_extension: Optional[DistanceIndicationExtension] = (
        field(
            default=None,
            metadata={
                "name": "DistanceIndicationExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
