from dataclasses import dataclass

from generated.location_property_type import LocationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Location(LocationPropertyType):
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml/3.2"
