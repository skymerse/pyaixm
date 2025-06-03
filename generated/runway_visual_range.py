from dataclasses import dataclass

from generated.runway_visual_range_type import RunwayVisualRangeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayVisualRange(RunwayVisualRangeType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
