from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmfeature_base_type import (
    AbstractAixmfeatureBaseType,
)
from pyaixm.generated.message_metadata_property_type import (
    MessageMetadataPropertyType,
)
from pyaixm.generated.sequence_number import SequenceNumber

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
