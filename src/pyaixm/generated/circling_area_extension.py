from dataclasses import dataclass

from generated.circling_area_extension_type import CirclingAreaExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class CirclingAreaExtension(CirclingAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
