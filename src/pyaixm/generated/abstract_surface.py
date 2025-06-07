from dataclasses import dataclass

from pyaixm.generated.abstract_surface_type import AbstractSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurface(AbstractSurfaceType):
    """
    The AbstractSurface element is the abstract head of the substitution group for
    all (continuous) surface elements.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
