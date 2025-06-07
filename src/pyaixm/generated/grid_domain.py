from dataclasses import dataclass

from pyaixm.generated.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridDomain(DomainSetType):
    class Meta:
        name = "gridDomain"
        namespace = "http://www.opengis.net/gml/3.2"
