from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.radio_communication_operational_status import (
    RadioCommunicationOperationalStatus,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationOperationalStatusPropertyType(
    AbstractAixmpropertyType
):
    radio_communication_operational_status: Optional[
        RadioCommunicationOperationalStatus
    ] = field(
        default=None,
        metadata={
            "name": "RadioCommunicationOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
