from dataclasses import dataclass

from generated.circling_area_type import CirclingAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingArea(CirclingAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
