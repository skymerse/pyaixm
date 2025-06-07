from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_topology_type import AbstractTopologyType
from pyaixm.generated.face_or_topo_solid_property_type import DirectedNode

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoPointType(AbstractTopologyType):
    directed_node: Optional[DirectedNode] = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
