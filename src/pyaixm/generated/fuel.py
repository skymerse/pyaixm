from dataclasses import dataclass

from generated.fuel_type import FuelType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Fuel(FuelType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
