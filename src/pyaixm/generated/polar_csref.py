from dataclasses import dataclass

from pyaixm.generated.polar_csproperty_type import PolarCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolarCsref(PolarCspropertyType):
    class Meta:
        name = "polarCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
