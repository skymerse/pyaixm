from dataclasses import dataclass

from pyaixm.generated.abstract_approach_leg_type import AbstractApproachLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractApproachLeg(AbstractApproachLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
