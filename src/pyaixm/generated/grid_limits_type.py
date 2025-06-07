from dataclasses import dataclass, field
from typing import Optional

from generated.grid_envelope_type import GridEnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridLimitsType:
    grid_envelope: Optional[GridEnvelopeType] = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
