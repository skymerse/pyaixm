from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.code_colour_type import CodeColourType
from generated.code_light_holding_position_type import (
    CodeLightHoldingPositionType,
)
from generated.code_light_intensity_type import CodeLightIntensityType
from generated.code_yes_no_type import CodeYesNoType
from generated.ground_lighting_availability_property_type import (
    GroundLightingAvailabilityPropertyType,
)
from generated.light_element_property_type import LightElementPropertyType
from generated.note_property_type import NotePropertyType
from generated.taxi_holding_position_light_system_time_slice_type_extension import (
    TaxiHoldingPositionLightSystemTimeSliceTypeExtension,
)
from generated.taxi_holding_position_property_type import (
    TaxiHoldingPositionPropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystemTimeSliceType(AbstractAixmtimeSliceType):
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
    type_value: Optional[CodeLightHoldingPositionType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    taxi_holding: Optional[TaxiHoldingPositionPropertyType] = field(
        default=None,
        metadata={
            "name": "taxiHolding",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[
        TaxiHoldingPositionLightSystemTimeSliceTypeExtension
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
