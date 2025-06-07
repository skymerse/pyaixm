from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_radar_equipment_type import (
    AbstractRadarEquipmentType,
)
from pyaixm.generated.precision_approach_radar_time_slice_property_type import (
    PrecisionApproachRadarTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrecisionApproachRadarType(AbstractRadarEquipmentType):
    time_slice: Iterable[PrecisionApproachRadarTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
