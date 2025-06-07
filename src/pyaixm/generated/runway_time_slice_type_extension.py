from dataclasses import dataclass, field
from typing import Optional

from generated.runway_extension_1 import RunwayExtension1
from generated.runway_extension_2 import RunwayExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_extension: Optional[RunwayExtension2] = field(
        default=None,
        metadata={
            "name": "RunwayExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_runway_extension: Optional[RunwayExtension1] = (
        field(
            default=None,
            metadata={
                "name": "RunwayExtension",
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
