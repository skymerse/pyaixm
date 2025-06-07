from dataclasses import dataclass

from pyaixm.generated.geodesic_string_type import GeodesicStringType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodesicString(GeodesicStringType):
    """A sequence of geodesic segments.

    The number of control points shall be at least two. interpolation is
    fixed as "geodesic". The content model follows the general pattern
    for the encoding of curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
