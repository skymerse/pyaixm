from dataclasses import dataclass

from generated.prime_meridian_property_type import PrimeMeridianPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PrimeMeridianRef(PrimeMeridianPropertyType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml/3.2"
