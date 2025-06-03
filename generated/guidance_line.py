from dataclasses import dataclass

from generated.guidance_line_type import GuidanceLineType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLine(GuidanceLineType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
