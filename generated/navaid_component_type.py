from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_position_in_ilstype import CodePositionInIlstype
from generated.code_yes_no_type import CodeYesNoType
from generated.navaid_component_type_extension import (
    NavaidComponentTypeExtension,
)
from generated.navaid_equipment_property_type import (
    NavaidEquipmentPropertyType,
)
from generated.no_sequence_type import NoSequenceType
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidComponentType(AbstractAixmobjectType):
    collocation_group: Optional[NoSequenceType] = field(
        default=None,
        metadata={
            "name": "collocationGroup",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    marker_position: Optional[CodePositionInIlstype] = field(
        default=None,
        metadata={
            "name": "markerPosition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    provides_navigable_location: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "providesNavigableLocation",
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
    extension: Iterable[NavaidComponentTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
