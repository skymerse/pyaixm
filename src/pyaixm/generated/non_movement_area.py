from dataclasses import dataclass

from generated.non_movement_area_type import NonMovementAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NonMovementArea(NonMovementAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
