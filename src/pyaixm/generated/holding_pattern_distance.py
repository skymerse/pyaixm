from dataclasses import dataclass

from pyaixm.generated.holding_pattern_distance_type import (
    HoldingPatternDistanceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternDistance(HoldingPatternDistanceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
