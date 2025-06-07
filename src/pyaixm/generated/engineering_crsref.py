from dataclasses import dataclass

from generated.engineering_crsproperty_type import EngineeringCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrsref(EngineeringCrspropertyType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
