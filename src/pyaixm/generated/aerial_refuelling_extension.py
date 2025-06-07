from dataclasses import dataclass

from pyaixm.generated.aerial_refuelling_extension_type import (
    AerialRefuellingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AerialRefuellingExtension(AerialRefuellingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
