from dataclasses import dataclass, field
from typing import Optional

from generated.dmeextension import Dmeextension
from generated.navaid_equipment_extension import NavaidEquipmentExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DmetimeSliceTypeExtension:
    class Meta:
        global_type = False

    dmeextension: Optional[Dmeextension] = field(
        default=None,
        metadata={
            "name": "DMEExtension",
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
