from dataclasses import dataclass

from generated.final_leg_extension_type import FinalLegExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class FinalLegExtension(FinalLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
