from dataclasses import dataclass

from pyaixm.generated.city_type import CityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class City(CityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
