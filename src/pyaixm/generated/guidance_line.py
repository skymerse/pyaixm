from dataclasses import dataclass

from pyaixm.generated.guidance_line_type import GuidanceLineType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLine(GuidanceLineType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
