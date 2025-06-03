from dataclasses import dataclass

from generated.quantity_extent_type import QuantityExtentType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class QuantityExtent(QuantityExtentType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
