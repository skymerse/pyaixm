from dataclasses import dataclass

from generated.multi_surface_type import MultiSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurface(MultiSurfaceType):
    """A gml:MultiSurface is defined by one or more gml:AbstractSurfaces.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:surfaceMember) or the array property
    (gml:surfaceMembers). It is also valid to use both the "standard"
    and the array properties in the same collection.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
