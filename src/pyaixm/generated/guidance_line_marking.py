from dataclasses import dataclass

from generated.guidance_line_marking_type import GuidanceLineMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineMarking(GuidanceLineMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
