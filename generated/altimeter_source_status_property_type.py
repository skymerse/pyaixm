from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.altimeter_source_status import AltimeterSourceStatus

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSourceStatusPropertyType(AbstractAixmpropertyType):
    altimeter_source_status: Optional[AltimeterSourceStatus] = field(
        default=None,
        metadata={
            "name": "AltimeterSourceStatus",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
