from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_approach_guidance_type import CodeApproachGuidanceType
from generated.code_direction_turn_type import CodeDirectionTurnType
from generated.code_lighting_jartype import CodeLightingJartype
from generated.code_marking_condition_type import CodeMarkingConditionType
from generated.code_runway_marking_type import CodeRunwayMarkingType
from generated.manoeuvring_area_availability_property_type import (
    ManoeuvringAreaAvailabilityPropertyType,
)
from generated.note_property_type import NotePropertyType
from generated.runway_direction_time_slice_type_extension import (
    RunwayDirectionTimeSliceTypeExtension,
)
from generated.runway_element_property_type import RunwayElementPropertyType
from generated.runway_property_type import RunwayPropertyType
from generated.text_designator_type import TextDesignatorType
from generated.val_angle_type import ValAngleType
from generated.val_bearing_type import ValBearingType
from generated.val_distance_type import ValDistanceType
from generated.val_distance_vertical_type import ValDistanceVerticalType
from generated.val_slope_type import ValSlopeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionTimeSliceType(AbstractAixmtimeSliceType):
    designator: Optional[TextDesignatorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    true_bearing: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "trueBearing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    true_bearing_accuracy: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "trueBearingAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    magnetic_bearing: Optional[ValBearingType] = field(
        default=None,
        metadata={
            "name": "magneticBearing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    pattern_vfr: Optional[CodeDirectionTurnType] = field(
        default=None,
        metadata={
            "name": "patternVFR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope_tdz: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "name": "slopeTDZ",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    elevation_tdz: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "elevationTDZ",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    elevation_tdzaccuracy: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "elevationTDZAccuracy",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_marking_type: Optional[CodeRunwayMarkingType] = field(
        default=None,
        metadata={
            "name": "approachMarkingType",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_marking_condition: Optional[CodeMarkingConditionType] = field(
        default=None,
        metadata={
            "name": "approachMarkingCondition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    class_lighting_jar: Optional[CodeLightingJartype] = field(
        default=None,
        metadata={
            "name": "classLightingJAR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    precision_approach_guidance: Optional[CodeApproachGuidanceType] = field(
        default=None,
        metadata={
            "name": "precisionApproachGuidance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    used_runway: Optional[RunwayPropertyType] = field(
        default=None,
        metadata={
            "name": "usedRunway",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    starting_element: Optional[RunwayElementPropertyType] = field(
        default=None,
        metadata={
            "name": "startingElement",
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
    availability: Iterable[ManoeuvringAreaAvailabilityPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[RunwayDirectionTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
