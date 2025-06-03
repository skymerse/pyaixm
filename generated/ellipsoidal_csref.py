from dataclasses import dataclass

from generated.ellipsoidal_csproperty_type import EllipsoidalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidalCsref(EllipsoidalCspropertyType):
    class Meta:
        name = "ellipsoidalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
