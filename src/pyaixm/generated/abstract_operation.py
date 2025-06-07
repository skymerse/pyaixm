from dataclasses import dataclass

from pyaixm.generated.sc_crs_property_type import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractOperation(AbstractCoordinateOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
