from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.apron_marking_extension_1 import ApronMarkingExtension1
from pyaixm.generated.apron_marking_extension_2 import ApronMarkingExtension2
from pyaixm.generated.marking_extension import MarkingExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    apron_marking_extension: Optional[ApronMarkingExtension2] = field(
        default=None,
        metadata={
            "name": "ApronMarkingExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_apron_marking_extension: Optional[
        ApronMarkingExtension1
    ] = field(
        default=None,
        metadata={
            "name": "ApronMarkingExtension",
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
