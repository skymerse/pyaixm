from dataclasses import dataclass

from pyaixm.generated.topo_point_property_type import TopoPointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointProperty(TopoPointPropertyType):
    """
    The gml:topoPointProperty property element may be used in features to express
    their relationship to the referenced topology node.
    """

    class Meta:
        name = "topoPointProperty"
        namespace = "http://www.opengis.net/gml/3.2"
