from dataclasses import dataclass

from generated.aerial_refuelling_point_type import AerialRefuellingPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingPoint(AerialRefuellingPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
