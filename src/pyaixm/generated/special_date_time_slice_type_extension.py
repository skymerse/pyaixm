from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.special_date_extension import SpecialDateExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialDateTimeSliceTypeExtension:
    class Meta:
        global_type = False

    special_date_extension: Optional[SpecialDateExtension] = field(
        default=None,
        metadata={
            "name": "SpecialDateExtension",
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
