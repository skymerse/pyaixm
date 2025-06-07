from dataclasses import dataclass

from pyaixm.generated.event_time_slice_type import EventTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class EventTimeSlice(EventTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
