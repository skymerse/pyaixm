from dataclasses import dataclass, field
from typing import Optional

from generated.navaid_extension_1 import NavaidExtension1
from generated.navaid_extension_2 import NavaidExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidTimeSliceTypeExtension:
    class Meta:
        global_type = False

    navaid_extension: Optional[NavaidExtension2] = field(
        default=None,
        metadata={
            "name": "NavaidExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_navaid_extension: Optional[NavaidExtension1] = (
        field(
            default=None,
            metadata={
                "name": "NavaidExtension",
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
