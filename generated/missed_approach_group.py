from dataclasses import dataclass

from generated.missed_approach_group_type import MissedApproachGroupType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachGroup(MissedApproachGroupType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
