from dataclasses import dataclass

from pyaixm.generated.surface_type_1 import SurfaceType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TriangulatedSurface(SurfaceType1):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.
    trianglePatches encapsulates the triangles of the triangulated
    surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
