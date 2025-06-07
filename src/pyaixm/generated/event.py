from dataclasses import dataclass

from pyaixm.generated.event_type import EventType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class Event(EventType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
