from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.event_extension import EventExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class EventTimeSliceTypeExtension:
    class Meta:
        global_type = False

    event_extension: Optional[EventExtension] = field(
        default=None,
        metadata={
            "name": "EventExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/extensions/FAA/FNSE",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
