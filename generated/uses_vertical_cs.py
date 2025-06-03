from dataclasses import dataclass

from generated.vertical_csproperty_type import VerticalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesVerticalCs(VerticalCspropertyType):
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml/3.2"
