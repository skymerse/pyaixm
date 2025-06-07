from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.callsign_detail import CallsignDetail

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CallsignDetailPropertyType(AbstractAixmpropertyType):
    callsign_detail: Optional[CallsignDetail] = field(
        default=None,
        metadata={
            "name": "CallsignDetail",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
