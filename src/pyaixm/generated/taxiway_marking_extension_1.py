from dataclasses import dataclass

from pyaixm.generated.taxiway_marking_extension_type_1 import (
    TaxiwayMarkingExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiwayMarkingExtension1(TaxiwayMarkingExtensionType1):
    class Meta:
        name = "TaxiwayMarkingExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
