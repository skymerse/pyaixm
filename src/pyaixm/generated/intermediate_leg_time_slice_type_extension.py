from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.approach_leg_extension import ApproachLegExtension
from pyaixm.generated.intermediate_leg_extension import (
    IntermediateLegExtension,
)
from pyaixm.generated.segment_leg_extension import SegmentLegExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class IntermediateLegTimeSliceTypeExtension:
    class Meta:
        global_type = False

    intermediate_leg_extension: Optional[IntermediateLegExtension] = field(
        default=None,
        metadata={
            "name": "IntermediateLegExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    approach_leg_extension: Optional[ApproachLegExtension] = field(
        default=None,
        metadata={
            "name": "ApproachLegExtension",
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
