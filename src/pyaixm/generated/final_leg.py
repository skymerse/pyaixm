from dataclasses import dataclass

from pyaixm.generated.final_leg_type import FinalLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalLeg(FinalLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
