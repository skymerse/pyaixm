from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_course_type import CodeCourseType
from generated.code_direction_turn_type import CodeDirectionTurnType
from generated.code_holding_usage_type import CodeHoldingUsageType
from generated.code_vertical_reference_type import CodeVerticalReferenceType
from generated.code_yes_no_type import CodeYesNoType
from generated.curve_property_type_2 import CurvePropertyType2
from generated.holding_pattern_distance_property_type import (
    HoldingPatternDistancePropertyType,
)
from generated.holding_pattern_duration_property_type import (
    HoldingPatternDurationPropertyType,
)
from generated.holding_pattern_time_slice_type_extension import (
    HoldingPatternTimeSliceTypeExtension,
)
from generated.note_property_type import NotePropertyType
from generated.segment_point_property_type import SegmentPointPropertyType
from generated.text_instruction_type import TextInstructionType
from generated.val_bearing_type import ValBearingType
from generated.val_distance_vertical_type import ValDistanceVerticalType
from generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternTimeSliceType(AbstractAixmtimeSliceType):
    type_value: Optional[CodeHoldingUsageType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_course: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "outboundCourse",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_course_type: Optional[CodeCourseType] = field(
        default=None,
        metadata={
            "name": "outboundCourseType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    inbound_course: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "inboundCourse",
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
    instruction: Optional[TextInstructionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    non_standard_holding: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "nonStandardHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_leg_span_end_time: Optional[
        HoldingPatternDurationPropertyType
    ] = field(
        default=None,
        metadata={
            "name": "outboundLegSpan_endTime",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_leg_span_end_distance: Optional[
        HoldingPatternDistancePropertyType
    ] = field(
        default=None,
        metadata={
            "name": "outboundLegSpan_endDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    outbound_leg_span_end_point: Optional[SegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "outboundLegSpan_endPoint",
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
    extent: Optional[CurvePropertyType2] = field(
        default=None,
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
    extension: Iterable[HoldingPatternTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
