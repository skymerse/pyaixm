from dataclasses import dataclass

from generated.degrees_type import DegreesType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml/3.2"
