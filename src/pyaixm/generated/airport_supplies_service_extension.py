from dataclasses import dataclass

from pyaixm.generated.airport_supplies_service_extension_type import (
    AirportSuppliesServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportSuppliesServiceExtension(AirportSuppliesServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
