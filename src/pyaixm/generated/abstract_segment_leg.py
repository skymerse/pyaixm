from dataclasses import dataclass

from pyaixm.generated.abstract_segment_leg_type import AbstractSegmentLegType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSegmentLeg(AbstractSegmentLegType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
