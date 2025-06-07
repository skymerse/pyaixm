from dataclasses import dataclass

from generated.deicing_area_type import DeicingAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingArea(DeicingAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
