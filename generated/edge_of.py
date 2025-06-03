from dataclasses import dataclass

from generated.curve_property_type_1 import CurvePropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EdgeOf(CurvePropertyType1):
    class Meta:
        name = "edgeOf"
        namespace = "http://www.opengis.net/gml/3.2"
