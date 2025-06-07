from dataclasses import dataclass

from generated.ellipsoid_property_type import EllipsoidPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidRef(EllipsoidPropertyType):
    class Meta:
        name = "ellipsoidRef"
        namespace = "http://www.opengis.net/gml/3.2"
