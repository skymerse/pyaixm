from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridEnvelopeType:
    low: Iterable[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        },
    )
    high: Iterable[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        },
    )
