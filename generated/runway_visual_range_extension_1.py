from dataclasses import dataclass

from generated.runway_visual_range_extension_type_1 import (
    RunwayVisualRangeExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayVisualRangeExtension1(RunwayVisualRangeExtensionType1):
    class Meta:
        name = "RunwayVisualRangeExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
