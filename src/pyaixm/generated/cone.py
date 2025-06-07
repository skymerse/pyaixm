from dataclasses import dataclass

from generated.cone_type import ConeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
