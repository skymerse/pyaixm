from dataclasses import dataclass

from pyaixm.generated.time_csproperty_type import TimeCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTimeCs(TimeCspropertyType):
    class Meta:
        name = "usesTimeCS"
        namespace = "http://www.opengis.net/gml/3.2"
