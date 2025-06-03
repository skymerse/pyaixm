from dataclasses import dataclass

from generated.topo_surface_type import TopoSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSurface(TopoSurfaceType):
    """Gml:TopoSurface represents a homogeneous topological expression, a set of
    directed faces, which if realised are isomorphic to a geometric surface
    primitive.

    The intended use of gml:TopoSurface is to appear within a surface
    feature to express the structural and possibly geometric
    relationships of this surface feature to other features via the
    shared face definitions.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
