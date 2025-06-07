from dataclasses import dataclass

from generated.geocentric_crsproperty_type import GeocentricCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeocentricCrsref(GeocentricCrspropertyType):
    class Meta:
        name = "geocentricCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
