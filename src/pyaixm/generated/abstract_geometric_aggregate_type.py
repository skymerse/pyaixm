from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_geometry_type import AbstractGeometryType
from generated.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
