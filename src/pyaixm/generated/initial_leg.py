from dataclasses import dataclass

from pyaixm.generated.initial_leg_type import InitialLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InitialLeg(InitialLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
