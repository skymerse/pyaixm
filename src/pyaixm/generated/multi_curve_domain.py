from dataclasses import dataclass

from generated.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveDomain(DomainSetType):
    class Meta:
        name = "multiCurveDomain"
        namespace = "http://www.opengis.net/gml/3.2"
