from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.marker_beacon_extension import MarkerBeaconExtension
from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkerBeaconTimeSliceTypeExtension:
    class Meta:
        global_type = False

    marker_beacon_extension: Optional[MarkerBeaconExtension] = field(
        default=None,
        metadata={
            "name": "MarkerBeaconExtension",
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
