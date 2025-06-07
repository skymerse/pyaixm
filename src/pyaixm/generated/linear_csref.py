from dataclasses import dataclass

from pyaixm.generated.linear_csproperty_type import LinearCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearCsref(LinearCspropertyType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
