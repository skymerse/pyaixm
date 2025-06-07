from dataclasses import dataclass

from pyaixm.generated.arrival_leg_type import ArrivalLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalLeg(ArrivalLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
