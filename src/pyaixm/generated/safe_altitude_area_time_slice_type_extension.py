from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.safe_altitude_area_extension import (
    SafeAltitudeAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    safe_altitude_area_extension: Optional[SafeAltitudeAreaExtension] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeAreaExtension",
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
