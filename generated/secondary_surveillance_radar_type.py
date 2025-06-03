from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_surveillance_radar_type import (
    AbstractSurveillanceRadarType,
)
from generated.secondary_surveillance_radar_time_slice_property_type import (
    SecondarySurveillanceRadarTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SecondarySurveillanceRadarType(AbstractSurveillanceRadarType):
    time_slice: Iterable[SecondarySurveillanceRadarTimeSlicePropertyType] = (
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
