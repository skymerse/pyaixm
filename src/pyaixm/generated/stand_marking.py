from dataclasses import dataclass

from generated.stand_marking_type import StandMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarking(StandMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
