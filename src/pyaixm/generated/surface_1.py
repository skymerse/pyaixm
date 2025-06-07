from dataclasses import dataclass

from pyaixm.generated.surface_type_1 import SurfaceType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Surface1(SurfaceType1):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """

    class Meta:
        name = "Surface"
        namespace = "http://www.opengis.net/gml/3.2"
