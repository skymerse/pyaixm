from dataclasses import dataclass

from generated.circle_by_center_point_type import CircleByCenterPointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CircleByCenterPoint(CircleByCenterPointType):
    """A gml:CircleByCenterPoint is an gml:ArcByCenterPoint with identical start
    and end angle to form a full circle.

    Again, this representation can be used only in 2D.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
