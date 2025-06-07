from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from pyaixm.generated.curve_members import CurveMembers
from pyaixm.generated.curve_property_type_1 import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    curve_member: Iterable[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve_members: Optional[CurveMembers] = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
