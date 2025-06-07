from dataclasses import dataclass

from pyaixm.generated.coordinates_type import CoordinatesType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Coordinates(CoordinatesType):
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml/3.2"
