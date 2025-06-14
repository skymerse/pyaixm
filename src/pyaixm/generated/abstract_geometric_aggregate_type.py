from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_geometry_type import AbstractGeometryType
from pyaixm.generated.aggregation_type import AggregationType

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
