from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.localizer_extension import LocalizerExtension
from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LocalizerTimeSliceTypeExtension:
    class Meta:
        global_type = False

    localizer_extension: Optional[LocalizerExtension] = field(
        default=None,
        metadata={
            "name": "LocalizerExtension",
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
