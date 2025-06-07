from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_protection_area_marking_extension import (
    AirportProtectionAreaMarkingExtension,
)
from pyaixm.generated.marking_extension import MarkingExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportProtectionAreaMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airport_protection_area_marking_extension: Optional[
        AirportProtectionAreaMarkingExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportProtectionAreaMarkingExtension",
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
