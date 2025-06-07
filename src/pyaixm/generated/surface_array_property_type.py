from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.elevated_surface import ElevatedSurface
from pyaixm.generated.polygon import Polygon
from pyaixm.generated.polyhedral_surface import PolyhedralSurface
from pyaixm.generated.surface_1 import Surface1
from pyaixm.generated.surface_2 import Surface2
from pyaixm.generated.surface_property_type_1 import (
    CompositeSurface,
    OrientableSurface,
)
from pyaixm.generated.tin import Tin
from pyaixm.generated.triangulated_surface import TriangulatedSurface

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceArrayPropertyType:
    """Gml:SurfaceArrayPropertyType is a container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """

    composite_surface: Iterable[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    orientable_surface: Iterable[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    elevated_surface: Iterable[ElevatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    surface: Iterable[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    tin: Iterable[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    triangulated_surface: Iterable[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    polyhedral_surface: Iterable[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    opengis_net_gml_3_2_surface: Iterable[Surface1] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    polygon: Iterable[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
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
