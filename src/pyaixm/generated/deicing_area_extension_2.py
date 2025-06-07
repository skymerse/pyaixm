from dataclasses import dataclass

from pyaixm.generated.deicing_area_extension_type_2 import (
    DeicingAreaExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class DeicingAreaExtension2(DeicingAreaExtensionType2):
    class Meta:
        name = "DeicingAreaExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
