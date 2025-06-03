from dataclasses import dataclass

from generated.taxiway_element_type import TaxiwayElementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayElement(TaxiwayElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
