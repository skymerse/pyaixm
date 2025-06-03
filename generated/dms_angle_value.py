from dataclasses import dataclass

from generated.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DmsAngleValue(DmsangleType):
    class Meta:
        name = "dmsAngleValue"
        namespace = "http://www.opengis.net/gml/3.2"
