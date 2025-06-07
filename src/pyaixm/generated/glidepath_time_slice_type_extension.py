from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.glidepath_extension import GlidepathExtension
from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GlidepathTimeSliceTypeExtension:
    class Meta:
        global_type = False

    glidepath_extension: Optional[GlidepathExtension] = field(
        default=None,
        metadata={
            "name": "GlidepathExtension",
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
