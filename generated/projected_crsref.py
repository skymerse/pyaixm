from dataclasses import dataclass

from generated.projected_crsproperty_type import ProjectedCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ProjectedCrsref(ProjectedCrspropertyType):
    class Meta:
        name = "projectedCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
