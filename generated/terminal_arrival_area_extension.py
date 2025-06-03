from dataclasses import dataclass

from generated.terminal_arrival_area_extension_type import (
    TerminalArrivalAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TerminalArrivalAreaExtension(TerminalArrivalAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
