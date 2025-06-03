from dataclasses import dataclass, field
from typing import Optional

from generated.vertical_structure_extension_1 import (
    VerticalStructureExtension1,
)
from generated.vertical_structure_extension_2 import (
    VerticalStructureExtension2,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureTimeSliceTypeExtension:
    class Meta:
        global_type = False

    vertical_structure_extension: Optional[VerticalStructureExtension2] = (
        field(
            default=None,
            metadata={
                "name": "VerticalStructureExtension",
                "type": "Element",
                "namespace": "urn:us.gov.dot.faa.aim.fns",
            },
        )
    )
    aixm_aero_schema_5_1_event_vertical_structure_extension: Optional[
        VerticalStructureExtension1
    ] = field(
        default=None,
        metadata={
            "name": "VerticalStructureExtension",
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
