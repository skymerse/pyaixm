from dataclasses import dataclass

from pyaixm.generated.surface_array_property_type import (
    SurfaceArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMembers(SurfaceArrayPropertyType):
    """This property element contains a list of surfaces.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "surfaceMembers"
        namespace = "http://www.opengis.net/gml/3.2"
