from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmtime_slice_type import (
    AbstractAixmtimeSliceType,
)
from pyaixm.generated.code_colour_type import CodeColourType
from pyaixm.generated.code_light_intensity_type import CodeLightIntensityType
from pyaixm.generated.code_side_type import CodeSideType
from pyaixm.generated.code_vasistype import CodeVasistype
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.ground_lighting_availability_property_type import (
    GroundLightingAvailabilityPropertyType,
)
from pyaixm.generated.light_element_property_type import (
    LightElementPropertyType,
)
from pyaixm.generated.no_number_type import NoNumberType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.visual_glide_slope_indicator_time_slice_type_extension import (
    VisualGlideSlopeIndicatorTimeSliceTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicatorTimeSliceType(AbstractAixmtimeSliceType):
    emergency_lighting: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "emergencyLighting",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    intensity_level: Optional[CodeLightIntensityType] = field(
        default=None,
        metadata={
            "name": "intensityLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    element: Iterable[LightElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    availability: Iterable[GroundLightingAvailabilityPropertyType] = field(
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
    type_value: Optional[CodeVasistype] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    position: Optional[CodeSideType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    number_box: Optional[NoNumberType] = field(
        default=None,
        metadata={
            "name": "numberBox",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    portable: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope_angle: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "slopeAngle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_eye_height_over_threshold: Optional[ValDistanceVerticalType] = (
        field(
            default=None,
            metadata={
                "name": "minimumEyeHeightOverThreshold",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "nillable": True,
            },
        )
    )
    runway_direction: Optional[RunwayDirectionPropertyType] = field(
        default=None,
        metadata={
            "name": "runwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[VisualGlideSlopeIndicatorTimeSliceTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
