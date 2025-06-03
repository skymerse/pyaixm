from dataclasses import dataclass

from generated.angle_indication_extension_type import (
    AngleIndicationExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AngleIndicationExtension(AngleIndicationExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
