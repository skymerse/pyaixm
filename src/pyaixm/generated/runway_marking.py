from dataclasses import dataclass

from generated.runway_marking_type import RunwayMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarking(RunwayMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
