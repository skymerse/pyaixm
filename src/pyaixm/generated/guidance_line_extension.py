from dataclasses import dataclass

from pyaixm.generated.guidance_line_extension_type import (
    GuidanceLineExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GuidanceLineExtension(GuidanceLineExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
