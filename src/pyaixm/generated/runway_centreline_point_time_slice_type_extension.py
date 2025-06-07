from dataclasses import dataclass, field
from typing import Optional

from generated.runway_centreline_point_extension import (
    RunwayCentrelinePointExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayCentrelinePointTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_centreline_point_extension: Optional[
        RunwayCentrelinePointExtension
    ] = field(
        default=None,
        metadata={
            "name": "RunwayCentrelinePointExtension",
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
