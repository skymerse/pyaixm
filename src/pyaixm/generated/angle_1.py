from dataclasses import dataclass

from pyaixm.generated.angle_type import AngleType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Angle1(AngleType):
    class Meta:
        name = "Angle"
        namespace = "http://www.isotc211.org/2005/gco"
