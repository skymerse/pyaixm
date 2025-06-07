from dataclasses import dataclass

from pyaixm.generated.runway_centreline_point_type import (
    RunwayCentrelinePointType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayCentrelinePoint(RunwayCentrelinePointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
