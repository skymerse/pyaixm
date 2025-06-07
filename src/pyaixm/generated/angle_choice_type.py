from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.angle_2 import Angle2
from pyaixm.generated.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AngleChoiceType:
    angle: Optional[Angle2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dms_angle: Optional[DmsAngle] = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
