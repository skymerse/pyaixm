from dataclasses import dataclass

from generated.marking_buoy_type import MarkingBuoyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingBuoy(MarkingBuoyType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
