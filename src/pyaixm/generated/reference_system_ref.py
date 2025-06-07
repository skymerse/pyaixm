from dataclasses import dataclass

from pyaixm.generated.sc_crs_property_type import CrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ReferenceSystemRef(CrspropertyType):
    class Meta:
        name = "referenceSystemRef"
        namespace = "http://www.opengis.net/gml/3.2"
