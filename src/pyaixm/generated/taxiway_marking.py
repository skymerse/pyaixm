from dataclasses import dataclass

from pyaixm.generated.taxiway_marking_type import TaxiwayMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayMarking(TaxiwayMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
