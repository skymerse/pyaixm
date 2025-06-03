from dataclasses import dataclass

from generated.vertical_structure_extension_type_2 import (
    VerticalStructureExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class VerticalStructureExtension2(VerticalStructureExtensionType2):
    class Meta:
        name = "VerticalStructureExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
