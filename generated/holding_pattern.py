from dataclasses import dataclass

from generated.holding_pattern_type import HoldingPatternType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPattern(HoldingPatternType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
