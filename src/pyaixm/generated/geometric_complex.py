from dataclasses import dataclass

from pyaixm.generated.geometric_complex_type import GeometricComplexType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricComplex(GeometricComplexType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
