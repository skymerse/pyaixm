from dataclasses import dataclass, field
from typing import Optional

from generated.runway_element_extension import RunwayElementExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayElementTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_element_extension: Optional[RunwayElementExtension] = field(
        default=None,
        metadata={
            "name": "RunwayElementExtension",
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
