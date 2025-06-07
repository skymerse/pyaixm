from dataclasses import dataclass

from pyaixm.generated.arrival_feeder_leg_type import ArrivalFeederLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalFeederLeg(ArrivalFeederLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
