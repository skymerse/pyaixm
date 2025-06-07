from dataclasses import dataclass

from pyaixm.generated.segment_leg_extension_type import SegmentLegExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SegmentLegExtension(SegmentLegExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
