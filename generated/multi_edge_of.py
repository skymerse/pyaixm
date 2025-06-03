from dataclasses import dataclass

from generated.multi_curve_property_type import MultiCurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiEdgeOf(MultiCurvePropertyType):
    class Meta:
        name = "multiEdgeOf"
        namespace = "http://www.opengis.net/gml/3.2"
