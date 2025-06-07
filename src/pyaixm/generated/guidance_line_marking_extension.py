from dataclasses import dataclass

from pyaixm.generated.guidance_line_marking_extension_type import (
    GuidanceLineMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GuidanceLineMarkingExtension(GuidanceLineMarkingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
