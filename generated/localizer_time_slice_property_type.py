from dataclasses import dataclass, field
from typing import Optional

from generated.localizer_time_slice import LocalizerTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class LocalizerTimeSlicePropertyType:
    localizer_time_slice: Optional[LocalizerTimeSlice] = field(
        default=None,
        metadata={
            "name": "LocalizerTimeSlice",
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
