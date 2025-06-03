from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from generated.altimeter_source_property_type import (
    AltimeterSourcePropertyType,
)
from generated.approach_condition_type_extension import (
    ApproachConditionTypeExtension,
)
from generated.circling_restriction_property_type import (
    CirclingRestrictionPropertyType,
)
from generated.code_minima_final_approach_path_type import (
    CodeMinimaFinalApproachPathType,
)
from generated.code_rnptype import CodeRnptype
from generated.landing_takeoff_area_collection_property_type import (
    LandingTakeoffAreaCollectionPropertyType,
)
from generated.minima_property_type import MinimaPropertyType
from generated.note_property_type import NotePropertyType
from generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from generated.val_slope_type import ValSlopeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachConditionType(AbstractAixmobjectType):
    final_approach_path: Optional[CodeMinimaFinalApproachPathType] = field(
        default=None,
        metadata={
            "name": "finalApproachPath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    required_navigation_performance: Optional[CodeRnptype] = field(
        default=None,
        metadata={
            "name": "requiredNavigationPerformance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    climb_gradient: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "name": "climbGradient",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_set: Optional[MinimaPropertyType] = field(
        default=None,
        metadata={
            "name": "minimumSet",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    circling_restriction: Iterable[CirclingRestrictionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "circlingRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aircraft_category: Iterable[AircraftCharacteristicPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "aircraftCategory",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    landing_area: Iterable[LandingTakeoffAreaCollectionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "landingArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altimeter: Optional[AltimeterSourcePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    design_surface: Iterable[ObstacleAssessmentAreaPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "designSurface",
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
    extension: Iterable[ApproachConditionTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
