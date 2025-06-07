from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.aircraft_characteristic_property_type import (
    AircraftCharacteristicPropertyType,
)
from pyaixm.generated.angle_indication_property_type import (
    AngleIndicationPropertyType,
)
from pyaixm.generated.code_altitude_use_type import CodeAltitudeUseType
from pyaixm.generated.code_course_type import CodeCourseType
from pyaixm.generated.code_direction_reference_type import (
    CodeDirectionReferenceType,
)
from pyaixm.generated.code_direction_turn_type import CodeDirectionTurnType
from pyaixm.generated.code_rnptype import CodeRnptype
from pyaixm.generated.code_segment_path_type import CodeSegmentPathType
from pyaixm.generated.code_segment_termination_type import (
    CodeSegmentTerminationType,
)
from pyaixm.generated.code_speed_reference_type import CodeSpeedReferenceType
from pyaixm.generated.code_trajectory_type import CodeTrajectoryType
from pyaixm.generated.code_vertical_reference_type import (
    CodeVerticalReferenceType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.curve_property_type_2 import CurvePropertyType2
from pyaixm.generated.departure_arrival_condition_property_type import (
    DepartureArrivalConditionPropertyType,
)
from pyaixm.generated.departure_leg_time_slice_type_extension import (
    DepartureLegTimeSliceTypeExtension,
)
from pyaixm.generated.distance_indication_property_type import (
    DistanceIndicationPropertyType,
)
from pyaixm.generated.holding_use_property_type import HoldingUsePropertyType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstacle_assessment_area_property_type import (
    ObstacleAssessmentAreaPropertyType,
)
from pyaixm.generated.standard_instrument_departure_property_type import (
    StandardInstrumentDeparturePropertyType,
)
from pyaixm.generated.terminal_segment_point_property_type import (
    TerminalSegmentPointPropertyType,
)
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_bearing_type import ValBearingType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_duration_type import ValDurationType
from pyaixm.generated.val_speed_type import ValSpeedType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureLegTimeSliceType(AbstractAixmtimeSliceType):
    end_condition_designator: Optional[CodeSegmentTerminationType] = field(
        default=None,
        metadata={
            "name": "endConditionDesignator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_path: Optional[CodeTrajectoryType] = field(
        default=None,
        metadata={
            "name": "legPath",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    leg_type_arinc: Optional[CodeSegmentPathType] = field(
        default=None,
        metadata={
            "name": "legTypeARINC",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    course: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    course_type: Optional[CodeCourseType] = field(
        default=None,
        metadata={
            "name": "courseType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    course_direction: Optional[CodeDirectionReferenceType] = field(
        default=None,
        metadata={
            "name": "courseDirection",
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
    speed_limit: Optional[ValSpeedType] = field(
        default=None,
        metadata={
            "name": "speedLimit",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_reference: Optional[CodeSpeedReferenceType] = field(
        default=None,
        metadata={
            "name": "speedReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    speed_interpretation: Optional[CodeAltitudeUseType] = field(
        default=None,
        metadata={
            "name": "speedInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    bank_angle: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "bankAngle",
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
    duration: Optional[ValDurationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    procedure_turn_required: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "procedureTurnRequired",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    upper_limit_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "upperLimitAltitude",
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
    lower_limit_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "lowerLimitAltitude",
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
    altitude_interpretation: Optional[CodeAltitudeUseType] = field(
        default=None,
        metadata={
            "name": "altitudeInterpretation",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_override_atc: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "altitudeOverrideATC",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_override_reference: Optional[CodeVerticalReferenceType] = field(
        default=None,
        metadata={
            "name": "altitudeOverrideReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    vertical_angle: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    start_point: Optional[TerminalSegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    end_point: Optional[TerminalSegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "endPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    trajectory: Optional[CurvePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    arc_centre: Optional[TerminalSegmentPointPropertyType] = field(
        default=None,
        metadata={
            "name": "arcCentre",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    angle: Optional[AngleIndicationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    distance: Optional[DistanceIndicationPropertyType] = field(
        default=None,
        metadata={
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
    holding: Optional[HoldingUsePropertyType] = field(
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
    required_navigation_performance: Optional[CodeRnptype] = field(
        default=None,
        metadata={
            "name": "requiredNavigationPerformance",
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
    departure: Optional[StandardInstrumentDeparturePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    condition: Iterable[DepartureArrivalConditionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[DepartureLegTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
