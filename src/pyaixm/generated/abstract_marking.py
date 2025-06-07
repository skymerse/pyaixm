from dataclasses import dataclass

from generated.abstract_marking_type import AbstractMarkingType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractMarking(AbstractMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
