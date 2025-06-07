from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.length_type import LengthType
from pyaixm.generated.line_string_segment_array_property_type import (
    LineStringSegmentArrayPropertyType,
)
from pyaixm.generated.surface_type_1 import SurfaceType1
from pyaixm.generated.tin_type_control_point import TinTypeControlPoint

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TinType(SurfaceType1):
    stop_lines: Iterable[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    break_lines: Iterable[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    max_length: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    control_point: Optional[TinTypeControlPoint] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
