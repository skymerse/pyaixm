from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxiway_marking_time_slice import TaxiwayMarkingTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayMarkingTimeSlicePropertyType:
    taxiway_marking_time_slice: Optional[TaxiwayMarkingTimeSlice] = field(
        default=None,
        metadata={
            "name": "TaxiwayMarkingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
