from dataclasses import dataclass, field
from typing import Optional

from generated.topo_volume import TopoVolume

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoVolumePropertyType:
    topo_volume: Optional[TopoVolume] = field(
        default=None,
        metadata={
            "name": "TopoVolume",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
