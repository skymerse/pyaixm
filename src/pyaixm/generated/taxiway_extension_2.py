from dataclasses import dataclass

from generated.taxiway_extension_type_2 import TaxiwayExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class TaxiwayExtension2(TaxiwayExtensionType2):
    class Meta:
        name = "TaxiwayExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
