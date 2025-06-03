from dataclasses import dataclass, field
from typing import Optional

from generated.marking_extension import MarkingExtension
from generated.runway_marking_extension_1 import RunwayMarkingExtension1
from generated.runway_marking_extension_2 import RunwayMarkingExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_marking_extension: Optional[RunwayMarkingExtension2] = field(
        default=None,
        metadata={
            "name": "RunwayMarkingExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_runway_marking_extension: Optional[
        RunwayMarkingExtension1
    ] = field(
        default=None,
        metadata={
            "name": "RunwayMarkingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    marking_extension: Optional[MarkingExtension] = field(
        default=None,
        metadata={
            "name": "MarkingExtension",
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
