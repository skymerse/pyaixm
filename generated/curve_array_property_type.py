from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.curve_property_type_1 import (
    CompositeCurve,
    Curve1,
    Curve2,
    ElevatedCurve,
    OrientableCurve,
)
from generated.line_string import LineString

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveArrayPropertyType:
    """A container for an array of curves.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """

    composite_curve: Iterable[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    orientable_curve: Iterable[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    elevated_curve: Iterable[ElevatedCurve] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedCurve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    curve: Iterable[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    opengis_net_gml_3_2_curve: Iterable[Curve1] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    line_string: Iterable[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
