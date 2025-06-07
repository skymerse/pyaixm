from dataclasses import dataclass

from pyaixm.generated.taxiway_light_system_type import TaxiwayLightSystemType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayLightSystem(TaxiwayLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
