from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxiway_light_system_time_slice import (
    TaxiwayLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayLightSystemTimeSlicePropertyType:
    taxiway_light_system_time_slice: Optional[TaxiwayLightSystemTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "TaxiwayLightSystemTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
