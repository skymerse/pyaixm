from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.vertical_structure_part import VerticalStructurePart

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructurePartPropertyType(AbstractAixmpropertyType):
    vertical_structure_part: Optional[VerticalStructurePart] = field(
        default=None,
        metadata={
            "name": "VerticalStructurePart",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
