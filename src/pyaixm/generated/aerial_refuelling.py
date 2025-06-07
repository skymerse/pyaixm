from dataclasses import dataclass

from pyaixm.generated.aerial_refuelling_type import AerialRefuellingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuelling(AerialRefuellingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
