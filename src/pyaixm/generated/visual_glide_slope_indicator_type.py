from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)
from pyaixm.generated.visual_glide_slope_indicator_time_slice_property_type import (
    VisualGlideSlopeIndicatorTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicatorType(AbstractGroundLightSystemType):
    time_slice: Iterable[VisualGlideSlopeIndicatorTimeSlicePropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "timeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "min_occurs": 1,
            },
        )
    )
