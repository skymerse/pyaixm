from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_hot_spot_extension import AirportHotSpotExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHotSpotTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airport_hot_spot_extension: Optional[AirportHotSpotExtension] = field(
        default=None,
        metadata={
            "name": "AirportHotSpotExtension",
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
