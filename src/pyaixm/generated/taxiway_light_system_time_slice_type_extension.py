from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ground_light_system_extension import (
    GroundLightSystemExtension,
)
from pyaixm.generated.taxiway_light_system_extension import (
    TaxiwayLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxiway_light_system_extension: Optional[TaxiwayLightSystemExtension] = (
        field(
            default=None,
            metadata={
                "name": "TaxiwayLightSystemExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    ground_light_system_extension: Optional[GroundLightSystemExtension] = (
        field(
            default=None,
            metadata={
                "name": "GroundLightSystemExtension",
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
