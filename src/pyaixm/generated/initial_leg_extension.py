from dataclasses import dataclass

from pyaixm.generated.initial_leg_extension_type import InitialLegExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class InitialLegExtension(InitialLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
