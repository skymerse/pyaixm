from dataclasses import dataclass

from pyaixm.generated.designated_point_type import DesignatedPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DesignatedPoint(DesignatedPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
