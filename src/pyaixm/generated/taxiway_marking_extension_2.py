from dataclasses import dataclass

from pyaixm.generated.taxiway_marking_extension_type_2 import (
    TaxiwayMarkingExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class TaxiwayMarkingExtension2(TaxiwayMarkingExtensionType2):
    class Meta:
        name = "TaxiwayMarkingExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
