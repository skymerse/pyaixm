from dataclasses import dataclass

from pyaixm.generated.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MappingRule(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
