from dataclasses import dataclass, field
from typing import Optional

from generated.navaid_equipment_extension import NavaidEquipmentExtension
from generated.sdfextension import Sdfextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SdftimeSliceTypeExtension:
    class Meta:
        global_type = False

    sdfextension: Optional[Sdfextension] = field(
        default=None,
        metadata={
            "name": "SDFExtension",
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
