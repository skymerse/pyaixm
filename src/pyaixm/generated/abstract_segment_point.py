from dataclasses import dataclass

from generated.abstract_segment_point_type import AbstractSegmentPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSegmentPoint(AbstractSegmentPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
