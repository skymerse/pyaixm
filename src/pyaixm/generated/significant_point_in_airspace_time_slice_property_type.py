from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.significant_point_in_airspace_time_slice import (
    SignificantPointInAirspaceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SignificantPointInAirspaceTimeSlicePropertyType:
    significant_point_in_airspace_time_slice: Optional[
        SignificantPointInAirspaceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SignificantPointInAirspaceTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
