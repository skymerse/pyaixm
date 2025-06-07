from dataclasses import dataclass

from pyaixm.generated.deicing_area_marking_type import DeicingAreaMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaMarking(DeicingAreaMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
