from dataclasses import dataclass

from pyaixm.generated.geodesic_type import GeodesicType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
