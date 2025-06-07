from dataclasses import dataclass

from generated.missed_approach_leg_type import MissedApproachLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachLeg(MissedApproachLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
