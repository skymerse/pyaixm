from dataclasses import dataclass

from pyaixm.generated.topo_complex_type import TopoComplexPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexProperty(TopoComplexPropertyType):
    class Meta:
        name = "topoComplexProperty"
        namespace = "http://www.opengis.net/gml/3.2"
