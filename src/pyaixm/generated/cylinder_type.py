from dataclasses import dataclass, field

from generated.abstract_gridded_surface_type import AbstractGriddedSurfaceType
from generated.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylinderType(AbstractGriddedSurfaceType):
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
        default=CurveInterpolationType.LINEAR,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        },
    )
