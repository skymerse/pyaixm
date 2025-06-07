from dataclasses import dataclass

from generated.holding_pattern_extension_type import (
    HoldingPatternExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class HoldingPatternExtension(HoldingPatternExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
