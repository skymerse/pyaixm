from dataclasses import dataclass, field
from typing import Optional

from generated.deicing_area_extension_1 import DeicingAreaExtension1
from generated.deicing_area_extension_2 import DeicingAreaExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    deicing_area_extension: Optional[DeicingAreaExtension2] = field(
        default=None,
        metadata={
            "name": "DeicingAreaExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_deicing_area_extension: Optional[
        DeicingAreaExtension1
    ] = field(
        default=None,
        metadata={
            "name": "DeicingAreaExtension",
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
