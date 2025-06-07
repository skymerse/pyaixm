from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from generated.abstract_topology_type import AbstractTopologyType
from generated.actuate_type import ActuateType
from generated.aggregation_type import AggregationType
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.show_type import ShowType
from generated.topo_primitive_member import TopoPrimitiveMember
from generated.topo_primitive_members import TopoPrimitiveMembers
from generated.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexType(AbstractTopologyType):
    maximal_complex: Optional["MaximalComplex"] = field(
        default=None,
        metadata={
            "name": "maximalComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    super_complex: Iterable["SuperComplex"] = field(
        default_factory=list,
        metadata={
            "name": "superComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    sub_complex: Iterable["SubComplex"] = field(
        default_factory=list,
        metadata={
            "name": "subComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_primitive_member: Iterable[TopoPrimitiveMember] = field(
        default_factory=list,
        metadata={
            "name": "topoPrimitiveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_primitive_members: Optional[TopoPrimitiveMembers] = field(
        default=None,
        metadata={
            "name": "topoPrimitiveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    is_maximal: bool = field(
        default=False,
        metadata={
            "name": "isMaximal",
            "type": "Attribute",
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
class TopoComplex(TopoComplexType):
    """Gml:TopoComplex is a collection of topological primitives.

    Each complex holds a reference to its maximal complex
    (gml:maximalComplex) and optionally to sub- or super-complexes
    (gml:subComplex, gml:superComplex). A topology complex contains its
    primitive and sub-complex members.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexPropertyType:
    topo_complex: Optional[TopoComplex] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
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


@dataclass
class MaximalComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "maximalComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SubComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "subComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SuperComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "superComplex"
        namespace = "http://www.opengis.net/gml/3.2"
