from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.azimuth_extension import AzimuthExtension
from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AzimuthTimeSliceTypeExtension:
    class Meta:
        global_type = False

    azimuth_extension: Optional[AzimuthExtension] = field(
        default=None,
        metadata={
            "name": "AzimuthExtension",
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
