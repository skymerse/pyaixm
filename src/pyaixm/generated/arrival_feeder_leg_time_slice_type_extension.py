from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.approach_leg_extension import ApproachLegExtension
from pyaixm.generated.arrival_feeder_leg_extension import (
    ArrivalFeederLegExtension,
)
from pyaixm.generated.segment_leg_extension import SegmentLegExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalFeederLegTimeSliceTypeExtension:
    class Meta:
        global_type = False

    arrival_feeder_leg_extension: Optional[ArrivalFeederLegExtension] = field(
        default=None,
        metadata={
            "name": "ArrivalFeederLegExtension",
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
