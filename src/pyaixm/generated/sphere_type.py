from dataclasses import dataclass, field

from pyaixm.generated.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)
from pyaixm.generated.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SphereType(AbstractGriddedSurfaceType):
    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        },
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        },
    )
