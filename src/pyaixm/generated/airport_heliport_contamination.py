from dataclasses import dataclass

from pyaixm.generated.airport_heliport_contamination_type import (
    AirportHeliportContaminationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportContamination(AirportHeliportContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
