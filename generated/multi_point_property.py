from dataclasses import dataclass

from generated.multi_point_property_type import MultiPointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.opengis.net/gml/3.2"
