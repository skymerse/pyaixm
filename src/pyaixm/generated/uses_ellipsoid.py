from dataclasses import dataclass

from pyaixm.generated.ellipsoid_property_type import EllipsoidPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEllipsoid(EllipsoidPropertyType):
    class Meta:
        name = "usesEllipsoid"
        namespace = "http://www.opengis.net/gml/3.2"
