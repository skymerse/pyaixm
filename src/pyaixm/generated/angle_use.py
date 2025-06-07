from dataclasses import dataclass

from pyaixm.generated.angle_use_type import AngleUseType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AngleUse(AngleUseType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
