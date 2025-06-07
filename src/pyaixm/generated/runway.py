from dataclasses import dataclass

from pyaixm.generated.runway_type import RunwayType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Runway(RunwayType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
