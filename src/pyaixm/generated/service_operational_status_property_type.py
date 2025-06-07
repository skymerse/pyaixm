from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.service_operational_status import ServiceOperationalStatus

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ServiceOperationalStatusPropertyType(AbstractAixmpropertyType):
    service_operational_status: Optional[ServiceOperationalStatus] = field(
        default=None,
        metadata={
            "name": "ServiceOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
