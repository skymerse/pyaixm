from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.ex_geographic_extent_property_type import (
    ExGeographicExtentPropertyType,
)
from generated.ex_temporal_extent_type import ExTemporalExtentType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExSpatialTemporalExtentType(ExTemporalExtentType):
    """
    Extent with respect to date and time.
    """

    class Meta:
        name = "EX_SpatialTemporalExtent_Type"

    spatial_extent: Iterable[ExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "spatialExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        },
    )
