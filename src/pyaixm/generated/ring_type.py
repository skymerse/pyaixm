from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_ring_type import AbstractRingType
from pyaixm.generated.aggregation_type import AggregationType
from pyaixm.generated.curve_property_type_1 import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RingType(AbstractRingType):
    curve_member: Iterable[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
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
