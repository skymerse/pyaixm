from dataclasses import dataclass

from generated.taxiway_type import TaxiwayType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Taxiway(TaxiwayType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
