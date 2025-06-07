from dataclasses import dataclass

from pyaixm.generated.point_property_type_1 import PointPropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointMember(PointPropertyType1):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """

    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"
