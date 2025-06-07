from dataclasses import dataclass

from pyaixm.generated.runway_marking_extension_type_1 import (
    RunwayMarkingExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayMarkingExtension1(RunwayMarkingExtensionType1):
    class Meta:
        name = "RunwayMarkingExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
