from dataclasses import dataclass

from pyaixm.generated.derived_crsproperty_type import DerivedCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrsref(DerivedCrspropertyType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
