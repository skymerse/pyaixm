from dataclasses import dataclass, field
from typing import Optional

from generated.angle_indication_extension import AngleIndicationExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleIndicationTimeSliceTypeExtension:
    class Meta:
        global_type = False

    angle_indication_extension: Optional[AngleIndicationExtension] = field(
        default=None,
        metadata={
            "name": "AngleIndicationExtension",
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
