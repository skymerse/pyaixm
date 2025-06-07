from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.arrival_leg_extension import ArrivalLegExtension
from pyaixm.generated.segment_leg_extension import SegmentLegExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalLegTimeSliceTypeExtension:
    class Meta:
        global_type = False

    arrival_leg_extension: Optional[ArrivalLegExtension] = field(
        default=None,
        metadata={
            "name": "ArrivalLegExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    segment_leg_extension: Optional[SegmentLegExtension] = field(
        default=None,
        metadata={
            "name": "SegmentLegExtension",
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
