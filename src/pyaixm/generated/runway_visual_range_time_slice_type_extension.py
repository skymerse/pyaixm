from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.runway_visual_range_extension_1 import (
    RunwayVisualRangeExtension1,
)
from pyaixm.generated.runway_visual_range_extension_2 import (
    RunwayVisualRangeExtension2,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayVisualRangeTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_visual_range_extension: Optional[RunwayVisualRangeExtension2] = (
        field(
            default=None,
            metadata={
                "name": "RunwayVisualRangeExtension",
                "type": "Element",
                "namespace": "urn:us.gov.dot.faa.aim.fns",
            },
        )
    )
    aixm_aero_schema_5_1_event_runway_visual_range_extension: Optional[
        RunwayVisualRangeExtension1
    ] = field(
        default=None,
        metadata={
            "name": "RunwayVisualRangeExtension",
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
