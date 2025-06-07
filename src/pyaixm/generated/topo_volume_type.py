from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_topology_type import AbstractTopologyType
from pyaixm.generated.aggregation_type import AggregationType
from pyaixm.generated.face_or_topo_solid_property_type import DirectedTopoSolid

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumeType(AbstractTopologyType):
    directed_topo_solid: Iterable[DirectedTopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
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
