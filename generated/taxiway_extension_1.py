from dataclasses import dataclass

from generated.taxiway_extension_type_1 import TaxiwayExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiwayExtension1(TaxiwayExtensionType1):
    class Meta:
        name = "TaxiwayExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
