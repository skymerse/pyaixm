from dataclasses import dataclass

from generated.surface_type_1 import SurfaceType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolyhedralSurface(SurfaceType1):
    """A polyhedral surface is a surface composed of polygon patches connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable. polygonPatches encapsulates the
    polygon patches of the polyhedral surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
