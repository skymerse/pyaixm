from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_obstacle_area_type import CodeObstacleAreaType
from generated.code_obstacle_assessment_surface_type import (
    CodeObstacleAssessmentSurfaceType,
)
from generated.note_property_type import NotePropertyType
from generated.obstacle_area_time_slice_type_extension import (
    ObstacleAreaTimeSliceTypeExtension,
)
from generated.organisation_authority_property_type import (
    OrganisationAuthorityPropertyType,
)
from generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from generated.surface_property_type_2 import SurfacePropertyType2
from generated.vertical_structure_property_type import (
    VerticalStructurePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAreaTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeObstacleAreaType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstruction_id_surface_condition: Optional[
        CodeObstacleAssessmentSurfaceType
    ] = field(
        default=None,
        metadata={
            "name": "obstructionIdSurfaceCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reference_owner_airport: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "reference_ownerAirport",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reference_owner_runway: Optional[RunwayDirectionPropertyType] = field(
        default=None,
        metadata={
            "name": "reference_ownerRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reference_owner_organisation: Optional[
        OrganisationAuthorityPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "reference_ownerOrganisation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_extent: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "name": "surfaceExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstacle: Iterable[VerticalStructurePropertyType] = field(
        default_factory=list,
        metadata={
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
    extension: Iterable[ObstacleAreaTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
