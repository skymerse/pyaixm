from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.significant_point_in_airspace_extension import (
    SignificantPointInAirspaceExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SignificantPointInAirspaceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    significant_point_in_airspace_extension: Optional[
        SignificantPointInAirspaceExtension
    ] = field(
        default=None,
        metadata={
            "name": "SignificantPointInAirspaceExtension",
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
