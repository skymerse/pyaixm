from dataclasses import dataclass

from pyaixm.generated.marking_buoy_extension_type import (
    MarkingBuoyExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class MarkingBuoyExtension(MarkingBuoyExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
