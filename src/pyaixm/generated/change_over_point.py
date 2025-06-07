from dataclasses import dataclass

from generated.change_over_point_type import ChangeOverPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ChangeOverPoint(ChangeOverPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
