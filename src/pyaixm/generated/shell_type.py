from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.aggregation_type import AggregationType
from pyaixm.generated.surface_property_type_1 import SurfaceMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ShellType:
    surface_member: Iterable[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
