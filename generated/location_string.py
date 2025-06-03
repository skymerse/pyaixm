from dataclasses import dataclass

from generated.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LocationString(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
