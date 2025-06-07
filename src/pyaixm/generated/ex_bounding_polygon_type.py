from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_ex_geographic_extent_type import (
    AbstractExGeographicExtentType,
)
from pyaixm.generated.gm_object_property_type import GmObjectPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExBoundingPolygonType(AbstractExGeographicExtentType):
    """
    Boundary enclosing the dataset expressed as the closed set of (x,y) coordinates
    of the polygon (last point replicates first point)
    """

    class Meta:
        name = "EX_BoundingPolygon_Type"

    polygon: Iterable[GmObjectPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
