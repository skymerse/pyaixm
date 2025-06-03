from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_surface_type import AbstractSurfaceType
from generated.actuate_type import ActuateType
from generated.aggregation_type import AggregationType
from generated.elevated_surface import ElevatedSurface
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.polygon import Polygon
from generated.polyhedral_surface import PolyhedralSurface
from generated.show_type import ShowType
from generated.sign_type import SignType
from generated.surface_1 import Surface1
from generated.surface_2 import Surface2
from generated.tin import Tin
from generated.triangulated_surface import TriangulatedSurface
from generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfacePropertyType1:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    class Meta:
        name = "SurfacePropertyType"

    composite_surface: Optional["CompositeSurface"] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_surface: Optional["OrientableSurface"] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevated_surface: Optional[ElevatedSurface] = field(
        default=None,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BaseSurface(SurfacePropertyType1):
    """The property baseSurface references or contains the base surface.

    The property baseSurface either references the base surface via the
    XLink-attributes or contains the surface element. A surface element
    is any element which is substitutable for gml:AbstractSurface. The
    base surface has positive orientation.
    """

    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMember(SurfacePropertyType1):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element, which is substitutable for
    gml:AbstractSurface.
    """

    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    surface_member: Iterable[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    base_surface: Optional[BaseSurface] = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompositeSurface(CompositeSurfaceType):
    """A gml:CompositeSurface is represented by a set of orientable surfaces.

    It is geometry type with all the geometric properties of a
    (primitive) surface. Essentially, a composite surface is a
    collection of surfaces that join in pairs on common boundary curves
    and which, when considered as a whole, form a single surface.
    surfaceMember references or contains inline one surface in the
    composite surface. The surfaces are contiguous.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a gml:AbstractSurface with an
    up-normal that reverses the direction for this OrientableSurface,
    the sense of "the top of the surface".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
