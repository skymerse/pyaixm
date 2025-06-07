from dataclasses import dataclass

from pyaixm.generated.topo_primitive_array_association_type import (
    TopoPrimitiveArrayAssociationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPrimitiveMembers(TopoPrimitiveArrayAssociationType):
    """
    The gml:topoPrimitiveMembers property element encodes the relationship between
    a topology complex and an arbitrary number of topology primitives.
    """

    class Meta:
        name = "topoPrimitiveMembers"
        namespace = "http://www.opengis.net/gml/3.2"
