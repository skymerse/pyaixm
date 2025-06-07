from dataclasses import dataclass

from pyaixm.generated.spherical_csproperty_type import SphericalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SphericalCsref(SphericalCspropertyType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
