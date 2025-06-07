from dataclasses import dataclass, field
from typing import Optional

from generated.airspace_extension import AirspaceExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airspace_extension: Optional[AirspaceExtension] = field(
        default=None,
        metadata={
            "name": "AirspaceExtension",
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
