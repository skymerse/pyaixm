from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.approach_lighting_system_time_slice_type_extension import (
    ApproachLightingSystemTimeSliceTypeExtension,
)
from generated.code_approach_lighting_icaotype import (
    CodeApproachLightingIcaotype,
)
from generated.code_approach_lighting_type import CodeApproachLightingType
from generated.code_colour_type import CodeColourType
from generated.code_light_intensity_type import CodeLightIntensityType
from generated.code_yes_no_type import CodeYesNoType
from generated.ground_lighting_availability_property_type import (
    GroundLightingAvailabilityPropertyType,
)
from generated.light_element_property_type import LightElementPropertyType
from generated.note_property_type import NotePropertyType
from generated.runway_direction_property_type import (
    RunwayDirectionPropertyType,
)
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystemTimeSliceType(AbstractAixmtimeSliceType):
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
    class_icao: Optional[CodeApproachLightingIcaotype] = field(
        default=None,
        metadata={
            "name": "classICAO",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeApproachLightingType] = field(
        default=None,
        metadata={
            "name": "type",
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
    sequenced_flashing: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "sequencedFlashing",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    alignment_indicator: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "alignmentIndicator",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    served_runway_direction: Optional[RunwayDirectionPropertyType] = field(
        default=None,
        metadata={
            "name": "servedRunwayDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[ApproachLightingSystemTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
