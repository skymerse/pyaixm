from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.circle_sector_property_type import CircleSectorPropertyType
from generated.code_navigation_area_restriction_type import (
    CodeNavigationAreaRestrictionType,
)
from generated.navigation_area_restriction_time_slice_type_extension import (
    NavigationAreaRestrictionTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from generated.procedure_property_type_2 import ProcedurePropertyType2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaRestrictionTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeNavigationAreaRestrictionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    procedure: Iterable[ProcedurePropertyType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    design_surface: Optional[ObstacleAssessmentAreaPropertyType] = field(
        default=None,
        metadata={
            "name": "designSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector_definition: Optional[CircleSectorPropertyType] = field(
        default=None,
        metadata={
            "name": "sectorDefinition",
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
    extension: Iterable[NavigationAreaRestrictionTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
