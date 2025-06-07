from dataclasses import dataclass, field
from typing import Optional

from generated.information_service_time_slice import (
    InformationServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationServiceTimeSlicePropertyType:
    information_service_time_slice: Optional[InformationServiceTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "InformationServiceTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
