from dataclasses import dataclass

from generated.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidDomain(DomainSetType):
    class Meta:
        name = "multiSolidDomain"
        namespace = "http://www.opengis.net/gml/3.2"
