from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airspace_border_crossing_extension import (
    AirspaceBorderCrossingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceBorderCrossingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airspace_border_crossing_extension: Optional[
        AirspaceBorderCrossingExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirspaceBorderCrossingExtension",
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
