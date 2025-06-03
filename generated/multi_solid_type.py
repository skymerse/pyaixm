from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from generated.solid_members import SolidMembers
from generated.solid_property_type import SolidMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    solid_member: Iterable[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
