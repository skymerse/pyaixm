from dataclasses import dataclass, field
from typing import Optional

from generated.navaid_equipment_extension import NavaidEquipmentExtension
from generated.vorextension import Vorextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VortimeSliceTypeExtension:
    class Meta:
        global_type = False

    vorextension: Optional[Vorextension] = field(
        default=None,
        metadata={
            "name": "VORExtension",
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
