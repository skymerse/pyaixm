from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.work_area_extension import WorkAreaExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    work_area_extension: Optional[WorkAreaExtension] = field(
        default=None,
        metadata={
            "name": "WorkAreaExtension",
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
