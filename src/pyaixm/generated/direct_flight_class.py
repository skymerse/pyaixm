from dataclasses import dataclass

from pyaixm.generated.direct_flight_class_type import DirectFlightClassType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectFlightClass(DirectFlightClassType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
