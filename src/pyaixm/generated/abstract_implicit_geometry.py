from dataclasses import dataclass

from pyaixm.generated.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractImplicitGeometry(AbstractGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
