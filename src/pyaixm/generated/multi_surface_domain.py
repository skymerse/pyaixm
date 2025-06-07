from dataclasses import dataclass

from pyaixm.generated.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfaceDomain(DomainSetType):
    class Meta:
        name = "multiSurfaceDomain"
        namespace = "http://www.opengis.net/gml/3.2"
