from dataclasses import dataclass

from generated.cylindrical_csproperty_type import CylindricalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCsref(CylindricalCspropertyType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
