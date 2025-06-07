from dataclasses import dataclass

from pyaixm.generated.arrival_feeder_leg_extension_type import (
    ArrivalFeederLegExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ArrivalFeederLegExtension(ArrivalFeederLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
