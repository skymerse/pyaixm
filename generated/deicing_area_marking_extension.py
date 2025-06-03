from dataclasses import dataclass

from generated.deicing_area_marking_extension_type import (
    DeicingAreaMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class DeicingAreaMarkingExtension(DeicingAreaMarkingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
