from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_curve_segment_type import AbstractCurveSegmentType
from generated.coordinates import Coordinates
from generated.curve_interpolation_type import CurveInterpolationType
from generated.knot_property_type import KnotPropertyType
from generated.knot_types_type import KnotTypesType
from generated.point_property import PointProperty
from generated.point_rep import PointRep
from generated.pos import Pos
from generated.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BsplineType(AbstractCurveSegmentType):
    class Meta:
        name = "BSplineType"

    pos: Iterable[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: Iterable[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_rep: Iterable[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    knot: Iterable[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
        },
    )
    interpolation: CurveInterpolationType = field(
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        },
    )
    is_polynomial: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        },
    )
    knot_type: Optional[KnotTypesType] = field(
        default=None,
        metadata={
            "name": "knotType",
            "type": "Attribute",
        },
    )
