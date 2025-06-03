from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.vertical_structure_lighting_status import (
    VerticalStructureLightingStatus,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureLightingStatusPropertyType(AbstractAixmpropertyType):
    vertical_structure_lighting_status: Optional[
        VerticalStructureLightingStatus
    ] = field(
        default=None,
        metadata={
            "name": "VerticalStructureLightingStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
