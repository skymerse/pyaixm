from dataclasses import dataclass

from generated.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsAngle(DmsangleType):
    class Meta:
        name = "dmsAngle"
        namespace = "http://www.opengis.net/gml/3.2"
