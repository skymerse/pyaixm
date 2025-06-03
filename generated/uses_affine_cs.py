from dataclasses import dataclass

from generated.affine_csproperty_type import AffineCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesAffineCs(AffineCspropertyType):
    class Meta:
        name = "usesAffineCS"
        namespace = "http://www.opengis.net/gml/3.2"
