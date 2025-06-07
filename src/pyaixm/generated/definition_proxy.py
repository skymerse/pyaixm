from dataclasses import dataclass

from pyaixm.generated.definition_proxy_type import DefinitionProxyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinitionProxy(DefinitionProxyType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
