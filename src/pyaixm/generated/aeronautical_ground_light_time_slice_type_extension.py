from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.aeronautical_ground_light_extension_1 import (
    AeronauticalGroundLightExtension1,
)
from pyaixm.generated.aeronautical_ground_light_extension_2 import (
    AeronauticalGroundLightExtension2,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AeronauticalGroundLightTimeSliceTypeExtension:
    class Meta:
        global_type = False

    aeronautical_ground_light_extension: Optional[
        AeronauticalGroundLightExtension2
    ] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLightExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_aeronautical_ground_light_extension: Optional[
        AeronauticalGroundLightExtension1
    ] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLightExtension",
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
