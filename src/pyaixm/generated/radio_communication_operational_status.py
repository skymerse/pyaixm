from dataclasses import dataclass

from pyaixm.generated.radio_communication_operational_status_type import (
    RadioCommunicationOperationalStatusType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadioCommunicationOperationalStatus(
    RadioCommunicationOperationalStatusType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
