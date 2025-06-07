from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.arresting_gear_extension import ArrestingGearExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrestingGearTimeSliceTypeExtension:
    class Meta:
        global_type = False

    arresting_gear_extension: Optional[ArrestingGearExtension] = field(
        default=None,
        metadata={
            "name": "ArrestingGearExtension",
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
