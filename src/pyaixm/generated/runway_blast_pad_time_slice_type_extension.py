from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.runway_blast_pad_extension import RunwayBlastPadExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayBlastPadTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_blast_pad_extension: Optional[RunwayBlastPadExtension] = field(
        default=None,
        metadata={
            "name": "RunwayBlastPadExtension",
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
