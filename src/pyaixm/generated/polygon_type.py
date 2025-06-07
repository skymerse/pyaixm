from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_surface_type import AbstractSurfaceType
from pyaixm.generated.exterior import Exterior
from pyaixm.generated.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonType(AbstractSurfaceType):
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
