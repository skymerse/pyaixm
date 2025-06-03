from dataclasses import dataclass

from generated.intermediate_leg_extension_type import (
    IntermediateLegExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class IntermediateLegExtension(IntermediateLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
