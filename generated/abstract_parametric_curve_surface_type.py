from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_surface_patch_type import AbstractSurfacePatchType
from generated.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
