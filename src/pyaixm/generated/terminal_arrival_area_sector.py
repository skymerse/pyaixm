from dataclasses import dataclass

from pyaixm.generated.terminal_arrival_area_sector_type import (
    TerminalArrivalAreaSectorType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaSector(TerminalArrivalAreaSectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
