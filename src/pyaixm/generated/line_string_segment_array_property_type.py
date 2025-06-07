from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.line_string_segment import LineStringSegment

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringSegmentArrayPropertyType:
    """
    Gml:LineStringSegmentArrayPropertyType provides a container for line strings.
    """

    line_string_segment: Iterable[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
