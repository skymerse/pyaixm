from dataclasses import dataclass

from pyaixm.generated.topo_surface_property_type import TopoSurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    """
    The gml:topoSurfaceProperty property element may be used in features to express
    their relationship to the referenced topology faces.
    """

    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"
