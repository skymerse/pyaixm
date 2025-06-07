from dataclasses import dataclass

from pyaixm.generated.runway_direction_extension_type_1 import (
    RunwayDirectionExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayDirectionExtension1(RunwayDirectionExtensionType1):
    class Meta:
        name = "RunwayDirectionExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
