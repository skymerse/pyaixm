from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_geometry_type import AbstractGeometryType
from generated.grid_envelope_type import GridEnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridType(AbstractGeometryType):
    grid_envelope: Optional[GridEnvelopeType] = field(
        default=None,
        metadata={
            "wrapper": "limits",
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    axis_labels: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        },
    )
    axis_name: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
