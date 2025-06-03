from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.no_sequence_type import NoSequenceType
from generated.note_property_type import NotePropertyType
from generated.radar_component_type_extension import (
    RadarComponentTypeExtension,
)
from generated.radar_equipment_property_type import RadarEquipmentPropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarComponentType(AbstractAixmobjectType):
    collocation_group: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "collocationGroup",
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
    the_radar_equipment: Optional[RadarEquipmentPropertyType] = field(
        default=None,
        metadata={
            "name": "theRadarEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    extension: Iterable[RadarComponentTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
