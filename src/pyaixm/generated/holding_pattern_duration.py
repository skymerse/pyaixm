from dataclasses import dataclass

from pyaixm.generated.holding_pattern_duration_type import (
    HoldingPatternDurationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternDuration(HoldingPatternDurationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
