from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.navaid_equipment_distance import NavaidEquipmentDistance

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidEquipmentDistancePropertyType(AbstractAixmpropertyType):
    navaid_equipment_distance: Optional[NavaidEquipmentDistance] = field(
        default=None,
        metadata={
            "name": "NavaidEquipmentDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
