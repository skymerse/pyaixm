from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.navaid_equipment_distance_type_extension import (
    NavaidEquipmentDistanceTypeExtension,
)
from generated.navaid_equipment_property_type import (
    NavaidEquipmentPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidEquipmentDistanceType(AbstractAixmobjectType):
    distance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    distance_accuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "distanceAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    the_navaid_equipment: Optional[NavaidEquipmentPropertyType] = field(
        default=None,
        metadata={
            "name": "theNavaidEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[NavaidEquipmentDistanceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
