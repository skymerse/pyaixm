from dataclasses import dataclass

from pyaixm.generated.elevated_point_type import ElevatedPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedPoint(ElevatedPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
