from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.designated_point_extension_1 import (
    DesignatedPointExtension1,
)
from pyaixm.generated.designated_point_extension_2 import (
    DesignatedPointExtension2,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DesignatedPointTimeSliceTypeExtension:
    class Meta:
        global_type = False

    designated_point_extension: Optional[DesignatedPointExtension2] = field(
        default=None,
        metadata={
            "name": "DesignatedPointExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_designated_point_extension: Optional[
        DesignatedPointExtension1
    ] = field(
        default=None,
        metadata={
            "name": "DesignatedPointExtension",
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
