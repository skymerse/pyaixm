from dataclasses import dataclass, field
from typing import Any

from pyaixm.generated.arc_by_center_point_type import ArcByCenterPointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CircleByCenterPointType(ArcByCenterPointType):
    start_angle: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    end_angle: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
