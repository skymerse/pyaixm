from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_surface_type import AbstractSurfaceType
from generated.patches import Patches
from generated.polygon_patches import PolygonPatches
from generated.triangle_patches import TrianglePatches

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceType1(AbstractSurfaceType):
    class Meta:
        name = "SurfaceType"

    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon_patches: Optional[PolygonPatches] = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
