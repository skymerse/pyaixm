from dataclasses import dataclass

from generated.spherical_csproperty_type import SphericalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesSphericalCs(SphericalCspropertyType):
    class Meta:
        name = "usesSphericalCS"
        namespace = "http://www.opengis.net/gml/3.2"
