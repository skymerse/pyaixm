from dataclasses import dataclass

from generated.solid_array_property_type import SolidArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidArrayProperty(SolidArrayPropertyType):
    class Meta:
        name = "solidArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"
