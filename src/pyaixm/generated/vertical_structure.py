from dataclasses import dataclass

from pyaixm.generated.vertical_structure_type import VerticalStructureType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructure(VerticalStructureType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
