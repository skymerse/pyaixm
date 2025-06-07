from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_runway_point_role_type import CodeRunwayPointRoleType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.navaid_equipment_distance_property_type import (
    NavaidEquipmentDistancePropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.runway_centreline_point_time_slice_type_extension import (
    RunwayCentrelinePointTimeSliceTypeExtension,
)
from generated.runway_declared_distance_property_type import (
    RunwayDeclaredDistancePropertyType,
)
from generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from generated.text_designator_type import TextDesignatorType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayCentrelinePointTimeSliceType(AbstractAixmtimeSliceType):
    role: Optional[CodeRunwayPointRoleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    on_runway: Optional[RunwayDirectionPropertyType] = field(
        default=None,
        metadata={
            "name": "onRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    associated_declared_distance: Iterable[
        RunwayDeclaredDistancePropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "associatedDeclaredDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    navaid_equipment: Iterable[NavaidEquipmentDistancePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "navaidEquipment",
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
    extension: Iterable[RunwayCentrelinePointTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
