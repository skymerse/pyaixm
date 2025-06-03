from dataclasses import dataclass

from generated.taxiway_contamination_type import TaxiwayContaminationType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayContamination(TaxiwayContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
