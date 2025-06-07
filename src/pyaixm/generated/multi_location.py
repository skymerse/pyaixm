from dataclasses import dataclass

from pyaixm.generated.multi_point_property_type import MultiPointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiLocation(MultiPointPropertyType):
    class Meta:
        name = "multiLocation"
        namespace = "http://www.opengis.net/gml/3.2"
