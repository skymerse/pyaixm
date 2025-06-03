from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmtime_slice_type import AbstractAixmtimeSliceType
from generated.aeronautical_ground_light_time_slice_type_extension import (
    AeronauticalGroundLightTimeSliceTypeExtension,
)
from generated.airport_heliport_property_type import (
    AirportHeliportPropertyType,
)
from generated.code_colour_type import CodeColourType
from generated.code_ground_lighting_type import CodeGroundLightingType
from generated.code_yes_no_type import CodeYesNoType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.note_property_type import NotePropertyType
from generated.text_name_type import TextNameType
from generated.vertical_structure_property_type import (
    VerticalStructurePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AeronauticalGroundLightTimeSliceType(AbstractAixmtimeSliceType):
    name: Optional[TextNameType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeGroundLightingType] = field(
        default=None,
        metadata={
            "name": "type",
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
    flashing: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    structure_beacon: Optional[VerticalStructurePropertyType] = field(
        default=None,
        metadata={
            "name": "structureBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    aerodrome_beacon: Optional[AirportHeliportPropertyType] = field(
        default=None,
        metadata={
            "name": "aerodromeBeacon",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    location: Optional[ElevatedPointPropertyType] = field(
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
    extension: Iterable[AeronauticalGroundLightTimeSliceTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
