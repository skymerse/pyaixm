from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.altimeter_source_extension import (
    AltimeterSourceExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSourceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    altimeter_source_extension: Optional[AltimeterSourceExtension] = field(
        default=None,
        metadata={
            "name": "AltimeterSourceExtension",
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
