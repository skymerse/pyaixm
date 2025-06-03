from dataclasses import dataclass

from generated.unplanned_holding_extension_type import (
    UnplannedHoldingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class UnplannedHoldingExtension(UnplannedHoldingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
