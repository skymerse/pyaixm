from dataclasses import dataclass

from generated.direction_finder_type import DirectionFinderType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectionFinder(DirectionFinderType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
