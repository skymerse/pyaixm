from dataclasses import dataclass

from pyaixm.generated.vertical_structure_extension_type_1 import (
    VerticalStructureExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class VerticalStructureExtension1(VerticalStructureExtensionType1):
    class Meta:
        name = "VerticalStructureExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
