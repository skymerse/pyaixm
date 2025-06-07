from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_colour_type import CodeColourType
from generated.code_marking_style_type import CodeMarkingStyleType
from generated.elevated_curve_property_type import ElevatedCurvePropertyType
from generated.elevated_point_property_type import ElevatedPointPropertyType
from generated.elevated_surface_property_type import (
    ElevatedSurfacePropertyType,
)
from generated.marking_element_type_extension import (
    MarkingElementTypeExtension,
)
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingElementType(AbstractAixmobjectType):
    colour: Optional[CodeColourType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    style: Optional[CodeMarkingStyleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent_surface_extent: Optional[ElevatedSurfacePropertyType] = field(
        default=None,
        metadata={
            "name": "extent_surfaceExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent_curve_extent: Optional[ElevatedCurvePropertyType] = field(
        default=None,
        metadata={
            "name": "extent_curveExtent",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent_location: Optional[ElevatedPointPropertyType] = field(
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
    extension: Iterable[MarkingElementTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
