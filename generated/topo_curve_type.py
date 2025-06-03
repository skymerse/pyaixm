from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_topology_type import AbstractTopologyType
from generated.aggregation_type import AggregationType
from generated.face_or_topo_solid_property_type import DirectedEdge

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoCurveType(AbstractTopologyType):
    directed_edge: Iterable[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
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
