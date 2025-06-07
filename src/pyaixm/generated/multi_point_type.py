from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from pyaixm.generated.point_member import PointMember
from pyaixm.generated.point_members import PointMembers

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    point_member: Iterable[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_members: Optional[PointMembers] = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
