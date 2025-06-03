from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.point_reference import PointReference

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PointReferencePropertyType(AbstractAixmpropertyType):
    point_reference: Optional[PointReference] = field(
        default=None,
        metadata={
            "name": "PointReference",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
