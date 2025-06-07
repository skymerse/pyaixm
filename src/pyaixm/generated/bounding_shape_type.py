from dataclasses import dataclass, field
from typing import Optional, Union

from generated.envelope import Envelope
from generated.envelope_with_time_period import EnvelopeWithTimePeriod
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.null import Null

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundingShapeType:
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    null: Optional[Null] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
