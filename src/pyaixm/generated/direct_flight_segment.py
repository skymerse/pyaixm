from dataclasses import dataclass

from pyaixm.generated.direct_flight_segment_type import DirectFlightSegmentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectFlightSegment(DirectFlightSegmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
