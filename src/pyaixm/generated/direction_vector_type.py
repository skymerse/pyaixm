from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.angle_type import AngleType
from pyaixm.generated.vector import Vector

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectionVectorType:
    """
    Direction vectors are specified by providing components of a vector.
    """

    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    horizontal_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
