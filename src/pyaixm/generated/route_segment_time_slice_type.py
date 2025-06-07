from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_direction_turn_type import CodeDirectionTurnType
from generated.code_level_type import CodeLevelType
from generated.code_rnptype import CodeRnptype
from generated.code_route_designator_suffix_type import (
    CodeRouteDesignatorSuffixType,
)
from generated.code_route_navigation_type import CodeRouteNavigationType
from generated.code_route_segment_path_type import CodeRouteSegmentPathType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.curve_property_type_2 import CurvePropertyType2
from generated.en_route_segment_point_property_type import (
    EnRouteSegmentPointPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from generated.route_availability_property_type import (
    RouteAvailabilityPropertyType,
)
from generated.route_property_type import RoutePropertyType
from generated.route_segment_time_slice_type_extension import (
    RouteSegmentTimeSliceTypeExtension,
)
from generated.val_bearing_type import ValBearingType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteSegmentTimeSliceType(AbstractAixmtimeSliceType):
    level: Optional[CodeLevelType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "upperLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    lower_limit_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "lowerLimitReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_obstacle_clearance_altitude: Optional[ValDistanceVerticalType] = (
        field(
            default=None,
            metadata={
                "name": "minimumObstacleClearanceAltitude",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    path_type: Optional[CodeRouteSegmentPathType] = field(
        default=None,
        metadata={
            "name": "pathType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    true_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "trueTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    magnetic_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "magneticTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reverse_true_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "reverseTrueTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    reverse_magnetic_track: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "reverseMagneticTrack",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    length: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width_left: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "widthLeft",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    width_right: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "widthRight",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    turn_direction: Optional[CodeDirectionTurnType] = field(
        default=None,
        metadata={
            "name": "turnDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    signal_gap: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "signalGap",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_enroute_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumEnrouteAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_crossing_at_end: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumCrossingAtEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_crossing_at_end_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "minimumCrossingAtEndReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    maximum_crossing_at_end: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "maximumCrossingAtEnd",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    maximum_crossing_at_end_reference: Optional[CodeVerticalReferenceType] = (
        field(
            default=None,
            metadata={
                "name": "maximumCrossingAtEndReference",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    navigation_type: Optional[CodeRouteNavigationType] = field(
        default=None,
        metadata={
            "name": "navigationType",
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
    designator_suffix: Optional[CodeRouteDesignatorSuffixType] = field(
        default=None,
        metadata={
            "name": "designatorSuffix",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start: Optional[EnRouteSegmentPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    route_formed: Optional[RoutePropertyType] = field(
        default=None,
        metadata={
            "name": "routeFormed",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    evaluation_area: Optional[ObstacleAssessmentAreaPropertyType] = field(
        default=None,
        metadata={
            "name": "evaluationArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    curve_extent: Optional[CurvePropertyType2] = field(
        default=None,
        metadata={
            "name": "curveExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end: Optional[EnRouteSegmentPointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[RouteAvailabilityPropertyType] = field(
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
    extension: Iterable[RouteSegmentTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
