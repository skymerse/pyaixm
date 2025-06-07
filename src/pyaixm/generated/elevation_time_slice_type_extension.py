from dataclasses import dataclass, field
from typing import Optional

from generated.elevation_extension import ElevationExtension
from generated.navaid_equipment_extension import NavaidEquipmentExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevationTimeSliceTypeExtension:
    class Meta:
        global_type = False

    elevation_extension: Optional[ElevationExtension] = field(
        default=None,
        metadata={
            "name": "ElevationExtension",
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
