from dataclasses import dataclass

from pyaixm.generated.airport_heliport_usage_type import (
    AirportHeliportUsageType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportUsage(AirportHeliportUsageType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
