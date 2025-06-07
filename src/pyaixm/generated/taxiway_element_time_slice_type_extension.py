from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxiway_element_extension import TaxiwayElementExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiwayElementTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxiway_element_extension: Optional[TaxiwayElementExtension] = field(
        default=None,
        metadata={
            "name": "TaxiwayElementExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
