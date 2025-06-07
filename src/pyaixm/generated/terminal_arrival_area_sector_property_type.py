from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.terminal_arrival_area_sector import (
    TerminalArrivalAreaSector,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaSectorPropertyType(AbstractAixmpropertyType):
    terminal_arrival_area_sector: Optional[TerminalArrivalAreaSector] = field(
        default=None,
        metadata={
            "name": "TerminalArrivalAreaSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
