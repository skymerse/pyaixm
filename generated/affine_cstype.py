from dataclasses import dataclass

from generated.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AffineCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "AffineCSType"
