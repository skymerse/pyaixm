from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_surveillance_radar_type import (
    AbstractSurveillanceRadarType,
)
from generated.primary_surveillance_radar_time_slice_property_type import (
    PrimarySurveillanceRadarTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadarType(AbstractSurveillanceRadarType):
    time_slice: Iterable[PrimarySurveillanceRadarTimeSlicePropertyType] = (
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
