from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.navaid_operational_status import NavaidOperationalStatus

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidOperationalStatusPropertyType(AbstractAixmpropertyType):
    navaid_operational_status: Optional[NavaidOperationalStatus] = field(
        default=None,
        metadata={
            "name": "NavaidOperationalStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
