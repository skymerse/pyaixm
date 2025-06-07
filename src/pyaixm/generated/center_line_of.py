from dataclasses import dataclass

from pyaixm.generated.curve_property_type_1 import CurvePropertyType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CenterLineOf(CurvePropertyType1):
    class Meta:
        name = "centerLineOf"
        namespace = "http://www.opengis.net/gml/3.2"
