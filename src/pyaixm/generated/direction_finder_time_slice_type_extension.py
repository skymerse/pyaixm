from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.direction_finder_extension import (
    DirectionFinderExtension,
)
from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectionFinderTimeSliceTypeExtension:
    class Meta:
        global_type = False

    direction_finder_extension: Optional[DirectionFinderExtension] = field(
        default=None,
        metadata={
            "name": "DirectionFinderExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    navaid_equipment_extension: Optional[NavaidEquipmentExtension] = field(
        default=None,
        metadata={
            "name": "NavaidEquipmentExtension",
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
