from dataclasses import dataclass

from pyaixm.generated.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "CylindricalCSType"
