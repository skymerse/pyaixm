from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.holding_assessment_time_slice_type_extension import (
    HoldingAssessmentTimeSliceTypeExtension,
)
from generated.holding_pattern_property_type import HoldingPatternPropertyType
from generated.note_property_type import NotePropertyType
from generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from generated.segment_point_property_type import SegmentPointPropertyType
from generated.text_name_type import TextNameType
from generated.unplanned_holding_property_type import (
    UnplannedHoldingPropertyType,
)
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType
from generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingAssessmentTimeSliceType(AbstractAixmtimeSliceType):
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
    speed_limit: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "name": "speedLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    pattern_template: Optional[TextNameType] = field(
        default=None,
        metadata={
            "name": "patternTemplate",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    turbulent_air: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "turbulentAir",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_length_toward: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "legLengthToward",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_length_away: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "legLengthAway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    holding_point: Optional[SegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "holdingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    unplanned_holding: Optional[UnplannedHoldingPropertyType] = field(
        default=None,
        metadata={
            "name": "unplannedHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    assessed_holding_pattern: Optional[HoldingPatternPropertyType] = field(
        default=None,
        metadata={
            "name": "assessedHoldingPattern",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstacle_assessment: Iterable[ObstacleAssessmentAreaPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "obstacleAssessment",
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
    extension: Iterable[HoldingAssessmentTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
