from dataclasses import dataclass

from generated.runway_visual_range_extension_type_2 import (
    RunwayVisualRangeExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayVisualRangeExtension2(RunwayVisualRangeExtensionType2):
    class Meta:
        name = "RunwayVisualRangeExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
