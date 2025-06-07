from dataclasses import dataclass

from pyaixm.generated.approach_leg_extension_type import (
    ApproachLegExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApproachLegExtension(ApproachLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
