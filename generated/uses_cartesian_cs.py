from dataclasses import dataclass

from generated.cartesian_csproperty_type import CartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesCartesianCs(CartesianCspropertyType):
    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"
