from dataclasses import dataclass, field
from typing import Optional

from generated.runway_direction_extension_1 import RunwayDirectionExtension1
from generated.runway_direction_extension_2 import RunwayDirectionExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_direction_extension: Optional[RunwayDirectionExtension2] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_runway_direction_extension: Optional[
        RunwayDirectionExtension1
    ] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionExtension",
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
