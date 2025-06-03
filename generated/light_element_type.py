from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_colour_type import CodeColourType
from generated.code_light_intensity_type import CodeLightIntensityType
from generated.code_light_source_type import CodeLightSourceType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.light_element_status_property_type import (
    LightElementStatusPropertyType,
)
from generated.light_element_type_extension import LightElementTypeExtension
from generated.note_property_type import NotePropertyType
from generated.val_light_intensity_type import ValLightIntensityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LightElementType(AbstractAixmobjectType):
    colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
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
    intensity: Optional[ValLightIntensityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    type_value: Optional[CodeLightSourceType] = field(
        default=None,
        metadata={
            "name": "type",
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
    availability: Iterable[LightElementStatusPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[LightElementTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
