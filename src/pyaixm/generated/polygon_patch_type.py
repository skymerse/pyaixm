from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from pyaixm.generated.exterior import Exterior
from pyaixm.generated.interior import Interior
from pyaixm.generated.surface_interpolation_type import (
    SurfaceInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: Iterable[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )
