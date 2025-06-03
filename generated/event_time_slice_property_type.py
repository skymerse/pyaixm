from dataclasses import dataclass, field
from typing import Optional

from generated.event_time_slice import EventTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class EventTimeSlicePropertyType:
    event_time_slice: Optional[EventTimeSlice] = field(
        default=None,
        metadata={
            "name": "EventTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
