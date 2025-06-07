from dataclasses import dataclass, field
from typing import Optional

from generated.navaid_equipment_extension import NavaidEquipmentExtension
from generated.ndbextension import Ndbextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NdbtimeSliceTypeExtension:
    class Meta:
        global_type = False

    ndbextension: Optional[Ndbextension] = field(
        default=None,
        metadata={
            "name": "NDBExtension",
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
