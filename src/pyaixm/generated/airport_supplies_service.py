from dataclasses import dataclass

from generated.airport_supplies_service_type import AirportSuppliesServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesService(AirportSuppliesServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
