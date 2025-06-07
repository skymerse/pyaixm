from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.navaid_equipment_extension import (
    NavaidEquipmentExtension,
)
from pyaixm.generated.tacanextension import Tacanextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TacantimeSliceTypeExtension:
    class Meta:
        global_type = False

    tacanextension: Optional[Tacanextension] = field(
        default=None,
        metadata={
            "name": "TACANExtension",
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
