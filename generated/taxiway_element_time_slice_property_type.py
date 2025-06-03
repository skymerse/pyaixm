from dataclasses import dataclass, field
from typing import Optional

from generated.taxiway_element_time_slice import TaxiwayElementTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayElementTimeSlicePropertyType:
    taxiway_element_time_slice: Optional[TaxiwayElementTimeSlice] = field(
        default=None,
        metadata={
            "name": "TaxiwayElementTimeSlice",
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
