from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmfeature_base_type import (
    AbstractAixmfeatureBaseType,
)
from generated.message_metadata_property_type import (
    MessageMetadataPropertyType,
)
from generated.sequence_number import SequenceNumber

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAixmmessageBaseType(AbstractAixmfeatureBaseType):
    class Meta:
        name = "AbstractAIXMMessageBaseType"

    sequence_number: Optional[SequenceNumber] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    message_metadata: Optional[MessageMetadataPropertyType] = field(
        default=None,
        metadata={
            "name": "messageMetadata",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
