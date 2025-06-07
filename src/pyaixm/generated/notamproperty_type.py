from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.notam import Notam

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NotampropertyType(AbstractAixmpropertyType):
    class Meta:
        name = "NOTAMPropertyType"

    notam: Optional[Notam] = field(
        default=None,
        metadata={
            "name": "NOTAM",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
            "required": True,
        },
    )
