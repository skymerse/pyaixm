from dataclasses import dataclass

from generated.missed_approach_leg_extension_type import (
    MissedApproachLegExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class MissedApproachLegExtension(MissedApproachLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
