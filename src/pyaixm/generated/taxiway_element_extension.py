from dataclasses import dataclass

from pyaixm.generated.taxiway_element_extension_type import (
    TaxiwayElementExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiwayElementExtension(TaxiwayElementExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
