from dataclasses import dataclass

from pyaixm.generated.vertical_crsproperty_type import VerticalCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCrsref(VerticalCrspropertyType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
