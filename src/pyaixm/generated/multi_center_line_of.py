from dataclasses import dataclass

from pyaixm.generated.multi_curve_property_type import MultiCurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCenterLineOf(MultiCurvePropertyType):
    class Meta:
        name = "multiCenterLineOf"
        namespace = "http://www.opengis.net/gml/3.2"
