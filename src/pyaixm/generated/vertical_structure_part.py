from dataclasses import dataclass

from pyaixm.generated.vertical_structure_part_type import (
    VerticalStructurePartType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructurePart(VerticalStructurePartType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
