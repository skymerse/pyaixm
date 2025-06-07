from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.unit_extension import UnitExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitTimeSliceTypeExtension:
    class Meta:
        global_type = False

    unit_extension: Optional[UnitExtension] = field(
        default=None,
        metadata={
            "name": "UnitExtension",
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
