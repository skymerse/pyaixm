from dataclasses import dataclass

from generated.sphere_type import SphereType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
